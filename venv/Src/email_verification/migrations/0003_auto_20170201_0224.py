# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_verification', '0002_email_encrypted_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='encrypted_email_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='email',
            name='verification_code',
            field=models.CharField(max_length=100),
        ),
    ]
