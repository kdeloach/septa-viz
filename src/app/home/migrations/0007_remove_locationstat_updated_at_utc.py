# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-27 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170227_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationstat',
            name='updated_at_utc',
        ),
    ]
