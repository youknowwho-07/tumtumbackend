# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170630_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='bus',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Bus'),
        ),
    ]