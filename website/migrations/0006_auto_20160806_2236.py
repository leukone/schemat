# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0005_auto_20160806_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(default=b'PROJECT', max_length=100),
        ),
    ]