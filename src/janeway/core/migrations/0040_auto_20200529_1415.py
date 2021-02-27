# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-29 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_fix_reviewer_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galley',
            name='type',
            field=models.CharField(choices=[('pdf', 'PDF'), ('epub', 'EPUB'), ('html', 'HTML'), ('xml', 'XML'), ('doc', 'Word (Doc)'), ('docx', 'Word (DOCX)'), ('odt', 'OpenDocument Text Document'), ('tex', 'LaTeX'), ('rtf', 'RTF'), ('other', 'Other')], max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('email', 'username')]),
        ),
    ]
