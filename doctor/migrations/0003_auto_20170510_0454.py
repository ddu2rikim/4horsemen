# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20170510_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateTimeField(),
        ),
    ]
