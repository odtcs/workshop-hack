# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengecompleted',
            name='challenge_id',
            field=models.IntegerField(unique=True),
        ),
    ]