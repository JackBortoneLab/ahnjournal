# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-08 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_remove_subscription_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]
