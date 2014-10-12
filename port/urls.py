#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.conf.urls import patterns, url

from port.views import DockListView


urlpatterns = patterns('',
    # Docks
    url(
        r'^docks/$',
        DockListView.as_view(),
        name='dock_list',
    ),

)