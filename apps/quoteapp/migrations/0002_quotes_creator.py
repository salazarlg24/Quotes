# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='creator',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
