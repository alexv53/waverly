# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waverly', '0002_auto_20170613_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='url_page',
            field=models.SlugField(blank=True),
        ),
    ]
