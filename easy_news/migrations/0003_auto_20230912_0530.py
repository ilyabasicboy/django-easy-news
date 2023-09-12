# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_news', '0002_auto__add_field_news_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date', 'title'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='Author', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Publication date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='short',
            field=tinymce.models.HTMLField(default=b'', verbose_name='Short description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Slug', unique_for_date=b'date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=tinymce.models.HTMLField(default=b'', verbose_name='Full text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
