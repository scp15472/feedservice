# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed_modules', '0005_auto_20181107_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 43, 17, 304280)),
        ),
        migrations.AlterField(
            model_name='downvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 43, 17, 307013)),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 43, 17, 305000)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 43, 17, 303732)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 43, 17, 306290)),
        ),
    ]
