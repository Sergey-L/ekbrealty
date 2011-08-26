# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from common.urls import urlpatterns as common_urls

urlpatterns = common_urls

# Serving static
if settings.DEBUG:
    urlpatterns += patterns('django.views',
        url(r'^media/(?P<path>.*)$', 'static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# Includes
urlpatterns += patterns('',
    (r'', include('seo.urls')),
)

urlpatterns += patterns('ektsite.views',
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^messages/$', 'message_list', name='message_list'),
    url(r'^messages/(.*)/$', 'message_list', name='message_list'),
    
    url(r'^realties/$', 'realty_list', name='realty_list'),
    url(r'^realties/(?P<id>\d+)/$', 'realty_detail', name='realty_detail'),
    url(r'^(?:specials)/$', 'items_list', name='items_list'),
    url(r'^add/$', 'add', name='add'),
)

urlpatterns += patterns('ektsite.views',
    url(r'^(?P<page_url>.*?)[/]{0,1}$', 'page', name="page"),
)