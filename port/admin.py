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
        'created_at',
        'updated_at',
    )

    raw_id_fields = ('ship', 'dock',)

    related_lookup_fields = {
        'fk': ['ship', 'dock'],
    }

    list_filter = ('is_active',)

    exclude = ('created_at', 'updated_at',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if obj and not obj.is_active:
            return False
        return True

    def get_actions(self, request):
        actions = super(ShipInDockAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ['is_active']
        return ['ship', 'dock']

admin.site.register(ShipInDock, ShipInDockAdmin)
