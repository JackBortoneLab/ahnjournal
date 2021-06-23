# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-05 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comms', '0003_auto_20210425_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='comments', to='comms.Comment'),
        ),
    ]