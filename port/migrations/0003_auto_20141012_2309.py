# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_shipindock_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipindock',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='container',
            name='ship',
            field=models.ForeignKey(related_name=b'containers', to='port.Ship'),
        ),
        migrations.AlterField(
            model_name='shipindock',
            name='dock',
            field=models.ForeignKey(related_name=b'ships', to='port.Dock'),
        ),
        migrations.AlterField(
            model_name='shipindock',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='ship is in the dock'),
        ),
    ]
