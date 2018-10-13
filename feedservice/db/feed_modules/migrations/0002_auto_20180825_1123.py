# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed_modules', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='questions',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='downvote',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='created_on',
        ),
        migrations.AddField(
            model_name='answer',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 25, 11, 23, 41, 399225)),
        ),
        migrations.AddField(
            model_name='downvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 25, 11, 23, 41, 401796)),
        ),
        migrations.AddField(
            model_name='question',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 25, 11, 23, 41, 399892)),
        ),
        migrations.AddField(
            model_name='topic',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 25, 11, 23, 41, 398697)),
        ),
        migrations.AddField(
            model_name='upvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 25, 11, 23, 41, 401243)),
        ),
    ]
