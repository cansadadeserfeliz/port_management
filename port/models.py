#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Ship(models.Model):
    name = models.CharField(
        max_length=36,
    )

    code = models.CharField(
        verbose_name=u'unique identifier',
        max_length=24,
        unique=True,
        validators=[RegexValidator(
            r'^[\d\w]+$',
            u'Ship identifier must be composed of letters and numbers',
        )],
    )

    @property
    def has_dangerous_goods(self):
        if self.containers.filter(has_dangerous_goods=True):
            return True
        return False

    def __unicode__(self):
        return u'{0}, {1}'.format(self.name, self.code)

    class Meta:
        ordering = ('name',)


class Container(models.Model):
    name = models.CharField(
        max_length=36,
    )

    ship = models.ForeignKey(
        'port.Ship',
        related_name='containers',
    )

    has_dangerous_goods = models.BooleanField(
        verbose_name=u'has a fire and/or chemical hazard.',
        default=False,
    )

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Dock(models.Model):
    name = models.CharField(
        max_length=36,
    )

    employees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )

    @property
    def get_current_ship(self):
        return self.ships.filter(is_active=True).first()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ShipInDock(models.Model):
    ship = models.ForeignKey(
        'port.Ship',
        related_name='ships',
    )

    dock = models.ForeignKey(
        'port.Dock',
        related_name='ships',
    )

    is_active = models.BooleanField(
        verbose_name=u'ship is in the dock',
        default=True,
    )

    created_at = models.DateTimeField(
        default=timezone.now,
    )

    updated_at = models.DateTimeField(
        default=timezone.now,
        auto_now=True,
    )

    def clean(self):
        if self.ship and self.dock and self.is_active:
            if ShipInDock.objects.filter(
                    dock=self.dock,
                    is_active=True
            ).exclude(id=self.id):
                raise ValidationError(u'A dock can contain only one ship at a time.')
        if self.ship and self.dock and self.is_active:
            if ShipInDock.objects.filter(
                    ship=self.ship,
                    is_active=True
            ).exclude(id=self.id):
                raise ValidationError(u'This ship is in another dock at this moment.')

    def __unicode__(self):
        return u'{0} in {1}'.format(self.ship.name, self.dock.name)

    class Meta:
        ordering = ('-updated_at',)