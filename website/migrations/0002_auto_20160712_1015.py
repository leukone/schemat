# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='store',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='chain',
            new_name='project',
        ),
    ]