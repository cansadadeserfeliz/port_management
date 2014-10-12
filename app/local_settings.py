#! /usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = True

TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'port_management',
        'USER': 'postgres',
        'PASSWORD': 'parol4ik',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}