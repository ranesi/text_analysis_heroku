# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-08 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='topics',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
