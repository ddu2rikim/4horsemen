# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 04:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0003_auto_20170505_1943'),
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='doctor_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]
