# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waverly', '0007_auto_20170620_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='url_website',
        ),
    ]