#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.views.generic import ListView
from django.views.generic import DetailView
from braces.views import LoginRequiredMixin

from port.models import Dock


class DockListView(LoginRequiredMixin, ListView):
    model = Dock
    context_object_name = 'docks'
    paginate_by = 5


class DockDetailView(LoginRequiredMixin, DetailView):
    model = Dock
    context_object_name = 'dock'