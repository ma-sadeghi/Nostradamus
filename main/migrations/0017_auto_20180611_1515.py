# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-11 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contest",
            name="users",
            field=models.ManyToManyField(
                related_name="contests", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
