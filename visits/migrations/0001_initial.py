# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 22:26
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0003_auto_20171113_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
                ('service', models.TextField(max_length=100, unique=True)),
                ('happened', models.BooleanField(default=False)),
                ('money_taken', models.PositiveIntegerField(null=True)),
                ('notes', models.TextField(blank=True, max_length=100)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.Animal')),
            ],
        ),
    ]
