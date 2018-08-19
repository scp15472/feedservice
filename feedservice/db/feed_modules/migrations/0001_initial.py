# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=1024)),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 39, 10, 675302))),
            ],
        ),
        migrations.CreateModel(
            name='Downvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 39, 10, 677785))),
                ('answer', models.ForeignKey(to='feed_modules.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=1024)),
                ('username', models.CharField(max_length=128)),
                ('views', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 39, 10, 675971))),
                ('answers', models.ManyToManyField(related_name='answers_for_questions', to='feed_modules.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 39, 10, 674740))),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 39, 10, 677240))),
                ('answer', models.ForeignKey(to='feed_modules.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(to='feed_modules.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(to='feed_modules.Question'),
        ),
    ]
