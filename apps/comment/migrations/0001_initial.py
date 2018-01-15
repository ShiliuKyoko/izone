# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-11 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '文章评论',
                'ordering': ['create_date'],
                'verbose_name_plural': '文章评论',
            },
        ),
    ]