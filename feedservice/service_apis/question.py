import django
from flask import jsonify, request
from flask_restful import Resource
from feedservice.db.feed_modules.models import Question as questions

django.setup()


class Question(Resource):
    def get(self):
       pass
    def post(self):
       pass

    def put(self):
        pass

    def delete(self):
       pass
