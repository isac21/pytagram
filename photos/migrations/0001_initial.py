# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photos.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, blank=True, verbose_name='One Line Description')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('image', photos.fields.ThumbnailImageField(upload_to='photo/%Y/%m')),
                ('description', models.TextField(blank=True, verbose_name='Photo Description')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
                ('album', models.ForeignKey(to='photos.Album')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
