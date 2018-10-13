# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed_modules', '0002_auto_20180825_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='downvote',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='upvote',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 12, 27, 48, 109914)),
        ),
        migrations.AlterField(
            model_name='downvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 12, 27, 48, 112432)),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 12, 27, 48, 110570)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 12, 27, 48, 109382)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 12, 27, 48, 111847)),
        ),
    ]
