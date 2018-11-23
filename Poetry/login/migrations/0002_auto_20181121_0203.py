# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-21 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(default=0)),
                ('flag', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm', models.CharField(max_length=240)),
                ('first_name', models.CharField(max_length=240)),
                ('second_name', models.CharField(max_length=240)),
                ('mobile', models.CharField(max_length=16)),
                ('image', models.ImageField(upload_to='profile/')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]