# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-20 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0041_issue_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='nav_sponsor',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='nav_review',
            field=models.BooleanField(default=False),
        ),
    ]
