# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0006_auto_20171113_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='importcacheentry',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='message_status',
            field=models.CharField(choices=[('no_information', 'No Information'), ('accepted', 'Sending'), ('delivered', 'Delivered'), ('failed', 'Failed')], default='no_information', max_length=255),
        ),
    ]
