# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0003_auto_20160804_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=b'/home/ola/Documents/schemat/drf_copy/drf_sample/client/static/app/images/2_mini.jpg', upload_to=b'blah'),
        ),
    ]