# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-21 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0050_auto_20210221_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='funding_target',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='funding_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
