#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.conf.urls import patterns, url

from port.views import DockListView
from port.views import DockDetailView


urlpatterns = patterns('',
    # Docks
    url(
        r'^docks/$',
        DockListView.as_view(),
        name='dock_list',
    ),

    # Docks
    url(
        r'^dock/(?P<pk>\d+)/$',
        DockDetailView.as_view(),
        name='dock_detail',
    ),
)