# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waverly', '0011_auto_20170702_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='url_audio10',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url_audio3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url_audio4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url_audio5',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url_audio6',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url_audio7',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url_audio8',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='url_audio9',
            field=models.URLField(blank=True, null=True),
        ),
    ]