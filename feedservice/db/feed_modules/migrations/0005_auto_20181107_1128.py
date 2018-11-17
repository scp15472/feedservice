# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed_modules', '0004_auto_20181107_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 28, 48, 716411)),
        ),
        migrations.AlterField(
            model_name='downvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 28, 48, 719516)),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 28, 48, 717144)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 28, 48, 715865)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 11, 28, 48, 718593)),
        ),
    ]
