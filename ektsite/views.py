# -*- coding: utf-8 -*-
import datetime
import random
import operator

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q

from common.utils import intlist, get_paginator
from common.fields import emails_list

from pages.models import Page, InfoBlock
from website.forms import SearchForm
from website.models import (Settings, Area, Region, DealType, RealtyType,
                            Realty, Gallery, Banner, Slot,)
from utils import get_url_params

def page(request, page_url):
    template = 'page.html'
    context = {}
    search_form = SearchForm(data=request.GET)
    if not page_url:
        template = 'index.html'
        try:
            rent_id = DealType.objects.get(name=u'Арендовать').id
            buy_id = DealType.objects.get(name=u'Купить').id
        except DealType.DoesNotExist:
            rent_id = ''
            buy_id = ''
        
        all_realty_url = get_url_params({'deal' : [rent_id, buy_id, ], })
        keys_show_rtl = RealtyType.objects.filter(ind_show=True)
        values_show_rtl = [get_url_params({'realty' : [item.id, ],
                                           'deal' : [rent_id, buy_id,]})
                           for item in keys_show_rtl]
        show_realty_type_dict = dict(zip(keys_show_rtl, values_show_rtl))
        
        keys_rtl = RealtyType.objects.all()
        values_rtl = [get_url_params({'realty' : [item.id, ],
                                      'deal' : [rent_id, buy_id,]})
                      for item in keys_rtl]
        realty_type_dict = dict(zip(keys_rtl, values_rtl))
        
        realty_list = Realty.objects.filter(region__name=u'Екатеринбург').order_by('-date')
        filter_realty_list = [realty_detail for realty_detail in realty_list
                               if (datetime.datetime.now()-realty_detail.date) < datetime.timedelta(hours=12000)][:8]
        sp_list = Realty.objects.filter(sp=True)
        try:
            sp_realty = random.choice(sp_list)
        except IndexError:
            sp_realty = None
        search_form = SearchForm()
        context = {'show_realty_type_dict' : show_realty_type_dict,
                   'realty_type_dict' : realty_type_dict,
                   'realty_list' : filter_realty_list,
                   'sp_realty' : sp_realty,
                   'all_realty_url' : all_realty_url,
                   'search_form' : search_form,}
    else:
        page = get_object_or_404(Page, path=page_url)
        template = 'page.html'
        context = {'show_search_form' : True,
                   'search_form' : search_form, }

    return render(request, template, context)

def realty_list(request):
    template = 'realty_list.html'
    rows_on_page = int(request.GET.get('rows', '1'))
    search_form = SearchForm(data=request.GET)
    query = request.GET.copy()
    
    args_fields = {}
    kwargs_fields = {}
    
    for item in query.items():
        if query.getlist(item[0]):
            if len(query.getlist(item[0])) < 2 :
                kwargs_fields[item[0]] = item[1]
            else:
                args_fields[item[0]] = query.getlist(item[0])
    
    kwargs = dict([(item[0], item[1]) for item in kwargs_fields.items()
        if item[1] and item[0] in [field.name for field in Realty._meta.fields]])
    realty_list = Realty.objects.filter(**kwargs)
    
    q = []
    for k, v in args_fields.iteritems():
        for id in range(len(v)):
            if v[id]:
                q.append( Q(**{'%s__id' % k : v[id]}))
        if q:
            q = reduce(operator.or_, q)
            realty_list = realty_list.filter(q)
            q = []
    
    sort_by = 'date'
    inv = 1
    if 'sort' in query.keys():
        if 'sort' in request.session.keys() and request.session['sort'] == query['sort']:
            inv = -int(query['inv'])
        else:
            query['inv'] = 1
        if inv > 0:
            realty_list = realty_list.order_by(query['sort'])
        else:
            realty_list = realty_list.order_by('-'+query['sort'])
        sort_by = query['sort']
        query['inv'] = inv
        request.session['sort'] = query['sort']
        del query['sort']
    else:
        request.session['sort'] = 'date'
        query['inv'] = 1
        realty_list = realty_list.order_by('date')
    
    object_list = get_paginator(request, realty_list, rows_on_page=rows_on_page)
    
    context = {'object_list' : object_list,
               'query' : query.urlencode,
               'inv' : inv,
               'sort_by' : sort_by,
               'search_form' : search_form, }
    
    return render(request, template, context)

def realty_detail(request, id):
    realty_detail = get_object_or_404(Realty, id=id)
    search_form = SearchForm(data=request.GET)
    
    section = int(request.GET.get('choice') or 1)
    
    if section == 1:
        template = 'realty_detail_desc.html'
    elif section == 2:
        template = 'realty_detail_desc.html'
    elif section == 3:
        template = 'realty_detail_desc.html'
    else:
        raise Http404()
    
    context = {'realty_detail' : realty_detail,
               'search_form' : search_form,}
    
    return render(request, template, context)

def add(request):
    return HttpResponse("add")

def items_list(request):
    context = {}
    template = 'items_list.html'
    return render(request, template, context)

def item_detail(request, id):
    return HttpResponse(id)

def message_list(request, arg=None):
    return render(request, 'messages.html')
        
def feedback(request):
    from website.forms import FeedbackForm
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = u'Вопрос с сайта'
            recipients = []
            recipients.extend(emails_list(request.settings.email))
            letter_context = form.cleaned_data
            letter_context.update({'site': request.settings.project})
            letter_content = render_to_string('feedback_letter.txt', letter_context)
            send_mail(subject, letter_content,
                      letter_context['email'] or recipients[0], recipients)
            messages.add_message(request, messages.SUCCESS, u"Ваше письмо успешно отправлено администрации сайта.")
            return redirect('')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})