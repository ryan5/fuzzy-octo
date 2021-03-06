# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171121_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='N|A'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
