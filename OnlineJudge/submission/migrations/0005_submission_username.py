# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_auto_20170509_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='username',
            field=models.CharField(default="", max_length=30),
            preserve_default=False,
        ),
    ]
