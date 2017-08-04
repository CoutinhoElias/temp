# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-02 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_author_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='author',
            name='title_author',
            field=models.CharField(default=1, max_length=100, verbose_name='Titulo Autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title1',
            field=models.CharField(default=1, max_length=100, verbose_name='Titulo 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title2',
            field=models.CharField(default=1, max_length=100, verbose_name='Titulo 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title3',
            field=models.CharField(default=1, max_length=100, verbose_name='Titulo 3'),
            preserve_default=False,
        ),
    ]
