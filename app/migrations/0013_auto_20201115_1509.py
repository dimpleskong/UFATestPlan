# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-15 07:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201107_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proeject',
            field=models.CharField(default='android', max_length=8, null=True, verbose_name='项目类型'),
        ),
        migrations.AlterField(
            model_name='functionallofic',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 15, 9, 48, 571967), verbose_name='更新时间'),
        ),
    ]