# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginapp', '0002_auto_20170201_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('plan', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('creator_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginapp.User')),
                ('users', models.ManyToManyField(related_name='destinations', to='loginapp.User')),
            ],
        ),
    ]
