#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    iban_number = models.CharField(
        verbose_name=u'IBAN bank account number',
        max_length=34,
        validators=[RegexValidator(
            r'^NL[\d\w]{16}$',
            u'For example, NL91ABNA0417164300',
        )],
        blank=True,
    )

    address = models.CharField(
        verbose_name=u'address',
        max_length=256,
    )

    def __unicode__(self):
        return self.get_full_name()

User._meta.get_field('is_staff').verbose_name = u'Is supervisor'
