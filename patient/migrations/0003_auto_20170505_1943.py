# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20170505_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patient',
            new_name='patient_id',
        ),
    ]
