# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20161023_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='website.Project'),
        ),
    ]
