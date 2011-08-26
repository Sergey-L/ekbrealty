# -*- coding: utf-8 -*-
import os, sys

MY_DJANGO_ROOT = os.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.sep)[:-2])
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(MY_DJANGO_ROOT)
sys.path.append(MY_DJANGO_ROOT+'/apps')
sys.path.append(PROJECT_DIR)

from common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_NAME = 'ekbrealty'
PROJECT_TITLE = 'EkbRealty.ru'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/db/%s.sqlite' % (PROJECT_DIR, PROJECT_NAME),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SITE_ID=1

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_DIR + '/media/'

STATIC_URL = MEDIA_URL
STATIC_ROOT = MEDIA_ROOT

ADMIN_MEDIA_PREFIX = '/admin_media/'
ADMIN_MEDIA_ROOT = MY_DJANGO_ROOT + '/admin_media/'

SECRET_KEY = '8!&d=_!md4nzvv0i658(vnyzdfdf_)-@b39g$_0+-oer3s0872'

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

TEMPLATE_DIRS = (
    PROJECT_DIR + "/website/templates",
    MY_DJANGO_ROOT + "/apps/common/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sites',
    'common',
    'filebrowser',
    'tinymce',
    'mptt',
    'treeadmin',
    'south',
    'seo',
    'pages',
    'website',
    'gallery',
	'smart_selects',
)

# MESSAGES
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# FILEBROWSER
FILEBROWSER_URL_FILEBROWSER_MEDIA = os.path.join(ADMIN_MEDIA_PREFIX , 'filebrowser/')
FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(ADMIN_MEDIA_ROOT , 'filebrowser/')
FILEBROWSER_URL_TINYMCE = os.path.join(ADMIN_MEDIA_PREFIX , 'tiny_mce/')
FILEBROWSER_PATH_TINYMCE = os.path.join(ADMIN_MEDIA_ROOT , 'tiny_mce/')

FILEBROWSER_VERSIONS_BASEDIR = '_versions_'

FILEBROWSER_ADMIN_THUMBNAIL ='fb_thumb'

FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': 'upscale'},
    'adv_index': {'verbose_name': u'Объявления на главной странице (105x70px)', 'width': 105, 'height': 70, 'opts': 'upscale'},
    'specadv_index': {'verbose_name': u'Спецпредложение на главной странице (230x140px)', 'width': 230, 'height': 140, 'opts': 'upscale'},
    'adv_search': {'verbose_name': u'Объявление в результатах поиска (70x47px)', 'width': 70, 'height': 47, 'opts': 'upscale'},
    'adv_big': {'verbose_name': u'Карточка объявления - большая картинка (350x22px)', 'width': 350, 'height': 22, 'opts': 'upscale'},
    'adv_bottom': {'verbose_name': u'Карточка объявления фотографии под ней (75x50px)', 'width': 75, 'height': 50, 'opts': 'upscale'},
    'like_objects': {'verbose_name': u'Похожие объекты (105x70px)', 'width': 105, 'height': 70, 'opts': 'upscale'},
}
FILEBROWSER_ADMIN_VERSIONS = ['fb_thumb','adv_index', 'specadv_index', 'adv_search', 'adv_big', 'adv_bottom', 'like_objects']

# CAPTCHA SETTINGS
# CAPTCHA SETTINGS
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '%s/cache' % PROJECT_DIR,
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
    #'default': {
    #    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #    'KEY_PREFIX': PROJECT_NAME,
    #    'LOCATION': '127.0.0.1:11211',
    #},
    #'default': {
    #    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    #}
}

CAPTCHA_CACHE_PREFIX = PROJECT_NAME+"_captcha_"
APPEND_SLASH = True

# TINYMCE SETTINGS
TINYMCE_JS_ROOT = os.path.join(ADMIN_MEDIA_ROOT, 'tiny_mce')
TINYMCE_JS_URL = os.path.join(ADMIN_MEDIA_PREFIX, 'tiny_mce/tiny_mce.js')