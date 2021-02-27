# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-03 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0032_auto_20190304_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='frozenauthor',
            name='is_corporate',
            field=models.BooleanField(default=False, help_text='If enabled, the institution and department fields will be used as the author full name'),
        ),
    ]
