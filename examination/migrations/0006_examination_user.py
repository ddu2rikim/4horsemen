# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 04:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examination', '0005_remove_examination_patient_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
