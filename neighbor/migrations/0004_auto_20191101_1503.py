# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-01 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0003_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ser',
            new_name='user',
        ),
    ]
