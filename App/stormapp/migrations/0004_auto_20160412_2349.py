# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stormapp', '0003_auto_20160412_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=b'static'),
        ),
    ]
