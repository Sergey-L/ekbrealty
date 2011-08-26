# -*- coding: utf-8 -*-
import random

from django.db import models
from django.core.cache import cache
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from common.fields import MultiEmailField
from filebrowser.fields import FileBrowseField
from tinymce import models as tinymce_models
from smart_selects.db_fields import ChainedForeignKey 
from smart_selects.db_fields import GroupedForeignKey
from gallery.models import Gallery

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^common\.fields\.MultiEmailField"])

class VisibleObjects(models.Manager):
    def get_query_set(self):
        return super(VisibleObjects, self).get_query_set().filter(visible=True)

class Settings(models.Model):
    project = models.CharField(u'Название проекта', max_length=255)
    email = MultiEmailField(u'Email для писем', max_length=255,
        help_text=u'''Можете вставить несколько email, разделив их запятой''')
    
    def __unicode__(self):
        return u'настройки'
            
    class Meta:
        verbose_name = u'настройки'
        verbose_name_plural = u'настройки'
@receiver(post_save, sender=Settings)
@receiver(post_delete, sender=Settings)
def clear_settings_cache(sender, **kwargs):
    cache.delete('settings')

class Region(models.Model):
    name = models.CharField(u'Название', max_length=255)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'регион'
        verbose_name_plural = u'регионы'

class Area(models.Model):
    name = models.CharField(u'Название', max_length=255)
    region = models.ForeignKey(Region, verbose_name=u'Регион')
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'район'
        verbose_name_plural = u'районы'
       
class DealType(models.Model):
    name = models.CharField(u'Название', max_length=255)
    slots = generic.GenericRelation('Slot', verbose_name = u'Слоты для баннеров')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'вид сделки'
        verbose_name_plural = u'виды сделок'

class RealtyType(models.Model):
    name = models.CharField(u'Название', max_length=255)
    slots = generic.GenericRelation('Slot', verbose_name = u'Слоты для баннеров')
    ind_show = models.BooleanField(u'Показывать на главной старнице', default=False)
    
    def __unicode__(self):
        return self.name   

    class Meta:
        verbose_name = u'вид недвижимости'
        verbose_name_plural = u'виды недвижимости'

class Realty(models.Model):
    name = models.CharField(u'Название', max_length=255)
    region = models.ForeignKey(Region, verbose_name=u'Регион')
    area = GroupedForeignKey(Area, ("region"), verbose_name=u'Район')
    realty = models.ForeignKey(RealtyType, verbose_name=u'Вид недвижимости')
    deal = models.ForeignKey(DealType, verbose_name=u'Вид сделки')
    address = models.CharField(u'Адрес', max_length=255)
    sq = models.FloatField(u'Площадь')
    cost = models.DecimalField(u'Стоимость', max_digits=15, decimal_places = 2)
    gallery = generic.GenericRelation(Gallery, verbose_name = u'Галлерея')#----
    date = models.DateTimeField(u'Дата публикации/изменения', auto_now_add=True)
    sp = models.BooleanField(u'Специальное предложение', default=False)
    content = tinymce_models.HTMLField(u'Контент')
    #-----test-----#
    phone = models.CharField(u'Телефон', max_length=255)
    email = models.CharField(u'Мыло', max_length=255)
    site = models.CharField(u'Сайт', max_length=255)
    infoblock = tinymce_models.HTMLField(verbose_name = 'HTML код')
    #--------------#
    
    #------SEO------#
    title = models.CharField(u'Заголовок)', max_length=255, blank=True)
    meta = models.TextField(u'Мета дескрипторы (meta)', blank=True, null=True)
    
    def __unicode__(self):
        return self.address
    
    def get_random_img(self):
        values = self.gallery.values()
        pos = random.choice(range(len(values)))
        return values[pos]['image']

    class Meta:
        verbose_name = u'объявление'
        verbose_name_plural = u'объявления'

class Profile(models.Model):
    user = models.OneToOneField(User)#----
    company_name = models.CharField(u'Название компании',blank=True,max_length=255)
    fio = models.CharField(u'ФИО',max_length=255)
    adress = models.CharField(u'Адресс',blank=True, max_length=255)
    email = models.EmailField(u'Email',max_length=255)
    phone =  models.CharField(u'Scype',max_length=255)
    icq = models.CharField(u'Scype',blank=True,max_length=255)
    scype = models.CharField(u'Scype',blank=True,max_length=255)
    comment = models.TextField(u'Комментарий',blank=True)
    
    def __unicode__(self):
        return self.fio
    
    class Meta:
        verbose_name = u'пользователь'
        verbose_name_plural = u'пользователи'

class Slot(models.Model):
    CHOICES =(
        ('top',u'Растяжка наверху'),
        ('text1',u'В тексте на главное странице'),
        ('right',u'Правый столбец в текст. стр.'),
        ('listadv',u'В списке объявлений'),
        ('listright',u'Правый столбец в списке'),
        ('listprofile',u'Справа в личном кабинете'),
    )
    name = models.CharField(u'Название',max_length=50)
    position = models.CharField(u'Область на странице', choices = CHOICES, max_length=50)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    cab_show = models.BooleanField(u'Отображать в личном кабинете', default=False)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
   
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'слот'
        verbose_name_plural = u'слоты'

class Banner(models.Model):
    name = models.CharField(u'Название',max_length=50)
    content = tinymce_models.HTMLField(verbose_name = 'HTML код')
    slots = models.ManyToManyField(Slot, verbose_name = u'Слоты для баннера')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'баннер'
        verbose_name_plural = u'баннеры'