# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20171113_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='motes',
            new_name='notes',
        ),
    ]
