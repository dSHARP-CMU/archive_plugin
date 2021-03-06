# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-28 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0025_auto_20190326_1252'),
        ('archive_plugin', '0002_remove_version_is_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.Issue')),
            ],
        ),
        migrations.RemoveField(
            model_name='version',
            name='revision_date',
        ),
    ]
