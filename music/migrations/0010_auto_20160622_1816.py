# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-22 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20160622_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='folder_name',
        ),
        migrations.AddField(
            model_name='folder',
            name='folder',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='folder',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
