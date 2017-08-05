# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waverly', '0005_auto_20170615_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_saved', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='podcast',
            old_name='date_added',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='name_slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverly.Podcast'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waverly.User'),
        ),
    ]