# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-18 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ins', '0003_auto_20180908_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='0')),
                ('friendname', models.TextField(default='0')),
            ],
        ),
    ]
