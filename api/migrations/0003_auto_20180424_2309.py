# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180424_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='pressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_speed',
            field=models.IntegerField(),
        ),
    ]