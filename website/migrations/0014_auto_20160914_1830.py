# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-14 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0013_contactinfo_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='contact_info',
            new_name='info',
        ),
    ]