# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170721_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='current_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]