#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.contrib import admin


from port.models import Ship
from port.models import Dock
from port.models import Container
from port.models import ShipInDock


class ContainerInline(admin.TabularInline):
    model = Container
    extra = 1


class ShipAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
    )

    inlines = [ContainerInline]

admin.site.register(Ship, ShipAdmin)


class DockAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    raw_id_fields = ('employees',)

    related_lookup_fields = {
        'm2m': ['employees'],
    }

admin.site.register(Dock, DockAdmin)


class ShipInDockAdmin(admin.ModelAdmin):
    list_display = (
        'ship',
        'dock',
        'is_active',
    )

    raw_id_fields = ('ship', 'dock',)

    related_lookup_fields = {
        'fk': ['ship', 'dock'],
    }

    list_filter = ('is_active',)

    exclude = ('created_at',)

admin.site.register(ShipInDock, ShipInDockAdmin)
