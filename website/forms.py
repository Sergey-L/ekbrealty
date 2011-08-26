# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from supercaptcha import CaptchaField
from smart_selects.form_fields import GroupedModelSelect

from website.models import (Region, Area, DealType, RealtyType, Realty)

def as_eul(self):
    return self._html_output(
        normal_row = u'<li%(html_class_attr)s><div class="FormLabel">%(label)s</div> <div class="FormField">%(field)s</div><div class="FormError">%(errors)s</div><div class="FormHelpText">%(help_text)s</div></li>',
        error_row = u'<li>%s</li>',
        row_ender = '</li>',
        help_text_html = u' %s',
        errors_on_separate_row = False)
forms.BaseForm.as_eul = as_eul

class SearchForm(forms.Form):
    region = forms.ModelChoiceField(Region.objects.all(), label=u'Регион', required=False)
    deal = forms.ModelChoiceField(DealType.objects.all(), label=u'Тип сделки', required=False)
    realty = forms.ModelChoiceField(RealtyType.objects.all(), label=u'Тип недвижимости', required=False)
    area = GroupedModelSelect(Area.objects.all(), 'region', required=False)
    lsq = forms.CharField(label=u'Площадь от', required=False)
    rsq = forms.CharField(label=u'Площадь до', required=False)
    lcost = forms.CharField(label=u'Стоимость от', required=False)
    rcost = forms.CharField(label=u'Стоимость до', required=False)
    lrent = forms.CharField(label=u'Стоимость в мес от', required=False)
    rrent = forms.CharField(label=u'Стоимость в мес до', required=False)
    
    #def __init__(self, *args, **kwargs):
    #    super(SearchForm, self).__init__(*args, **kwargs)
    #
    #    for key in self.fields:
    #        self.fields[key].required = False
    
    #class Meta:
    #    fields = ('region' ,'deal', 'realty', 'area',)
    #    model = Realty

class FeedbackForm(forms.Form):
    fio = forms.CharField(label=u'Ваше имя')
    phones = forms.CharField(label=u'Контактный телефон', required=False)
    email = forms.EmailField(label=u'Email')
    comment = forms.CharField(label=u'Комментарий', widget=forms.Textarea)
    captcha = CaptchaField(label=u'Защита от роботов')