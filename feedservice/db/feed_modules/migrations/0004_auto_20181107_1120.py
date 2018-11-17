# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed_modules', '0003_auto_20180830_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 20, 35, 635263)),
        ),
        migrations.AlterField(
            model_name='downvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 20, 35, 638003)),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 20, 35, 635938)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 20, 35, 634722)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 20, 35, 637235)),
        ),
    ]
