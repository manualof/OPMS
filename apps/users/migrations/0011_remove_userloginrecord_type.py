# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180105_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userloginrecord',
            name='type',
        ),
    ]