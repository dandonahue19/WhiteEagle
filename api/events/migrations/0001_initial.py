# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-20 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dt', models.DateTimeField()),
                ('dt_end', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventType'),
        ),
    ]
