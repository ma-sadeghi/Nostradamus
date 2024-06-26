# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-07 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_auto_20170621_2105"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="team1_name",
            new_name="away",
        ),
        migrations.RenameField(
            model_name="game",
            old_name="team1_shortname",
            new_name="away_abbreviation",
        ),
        migrations.RenameField(
            model_name="game",
            old_name="team1_score",
            new_name="away_score",
        ),
        migrations.RenameField(
            model_name="game",
            old_name="team2_name",
            new_name="home",
        ),
        migrations.RenameField(
            model_name="game",
            old_name="team2_shortname",
            new_name="home_abbreviation",
        ),
        migrations.RenameField(
            model_name="game",
            old_name="team2_score",
            new_name="home_score",
        ),
    ]
