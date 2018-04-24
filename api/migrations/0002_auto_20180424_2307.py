# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='pressure',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='weather',
            name='temperature',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='weather',
            name='wind_speed',
            field=models.IntegerField(default=0),
        ),
    ]
