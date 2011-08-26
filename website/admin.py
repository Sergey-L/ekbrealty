# -*- coding: utf-8 -*-
from django.contrib import admin
from website.models import (Settings, Area, Region, DealType, RealtyType,
                            Realty, Gallery, Banner, Slot,)
from django.contrib.contenttypes import generic
from django.forms import CheckboxSelectMultiple
from django.db import models

from models import Gallery


class BannerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class AreaInline(admin.TabularInline):
    model = Area

class GalleryInline(generic.GenericTabularInline):
    model = Gallery
    
class SlotsInline(generic.GenericTabularInline):
    model = Slot
    
class RealtyAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline
    ]

class RegionAdmin(admin.ModelAdmin):
    inlines = [
        AreaInline,
    ]
    
class SlotAdmin(admin.ModelAdmin):
    inlines = [
        SlotsInline,
    ]
    
admin.site.register(Settings)
admin.site.register(Region,RegionAdmin)
admin.site.register(DealType,SlotAdmin)
admin.site.register(RealtyType,SlotAdmin)
admin.site.register(Realty, RealtyAdmin)
admin.site.register(Gallery)
admin.site.register(Banner,BannerAdmin)
admin.site.register(Slot)