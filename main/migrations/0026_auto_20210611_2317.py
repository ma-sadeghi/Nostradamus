# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2021-06-12 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0025_merge_20180630_1240"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
