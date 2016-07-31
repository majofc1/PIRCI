# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividad', '0013_auto_20160730_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialDeVisitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='user1', max_length=90)),
                ('evento', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userTitle', models.CharField(default='user1', max_length=90)),
            ],
        ),
    ]
