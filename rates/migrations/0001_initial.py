# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-29 16:13
from __future__ import unicode_literals

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ECBRate",
            fields=[
                ("dt", models.DateField(primary_key=True, serialize=False)),
                ("rate_3m", models.FloatField()),
                ("rate_4m", models.FloatField()),
                ("rate_6m", models.FloatField()),
                ("rate_9m", models.FloatField()),
                ("rate_1y", models.FloatField()),
                ("rate_2y", models.FloatField()),
                ("rate_5y", models.FloatField()),
                ("rate_7y", models.FloatField()),
                ("rate_10y", models.FloatField()),
                ("rate_15y", models.FloatField()),
                ("rate_30y", models.FloatField()),
            ],
        )
    ]