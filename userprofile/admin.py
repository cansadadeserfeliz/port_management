#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserChangeForm
from django.contrib.auth.admin import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

admin.site.register(User, UserAdmin)