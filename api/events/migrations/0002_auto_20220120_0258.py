# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-20 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dow',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='reoccuring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
