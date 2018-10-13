from datetime import datetime
from django.db import models

class Topic(models.Model):
    topic_id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    create_on = models.DateTimeField(default=datetime.now())

class Answer(models.Model):
    question = models.ForeignKey('Question')
    string = models.CharField(max_length=1024)
    username = models.CharField(max_length=128)
    create_on = models.DateTimeField(default=datetime.now())

class Question(models.Model):
    topic = models.ForeignKey(Topic)
    string = models.CharField(max_length=1024)
    username = models.CharField(max_length=128)
    answers = models.ManyToManyField(Answer,related_name='answers_for_questions')
    views = models.IntegerField(null=True)
    create_on = models.DateTimeField(default=datetime.now())

class Upvote(models.Model):
    username = models.CharField(max_length=128)
    answer = models.ForeignKey(Answer)
    is_active = models.BooleanField(default=True)
    create_on = models.DateTimeField(default=datetime.now())

class Downvote(models.Model):
    username = models.CharField(max_length=128)
    answer = models.ForeignKey(Answer)
    is_active = models.BooleanField(default=True)
    create_on = models.DateTimeField(default=datetime.now())

