# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_auto_20180208_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portmap',
            name='status',
        ),
    ]