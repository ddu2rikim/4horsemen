# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20170505_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_id',
            new_name='patient',
        ),
    ]