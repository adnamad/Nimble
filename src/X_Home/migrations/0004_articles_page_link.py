# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-01 12:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('X_Home', '0003_articles_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='page_link',
            field=models.CharField(default=datetime.datetime(2016, 10, 1, 12, 51, 27, 391792, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]