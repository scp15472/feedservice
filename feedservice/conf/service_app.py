from flask import Flask
from flask_restful import Api
import django

from feedservice.service_apis.answer import Answer
from feedservice.service_apis.downvote import Downvote
from feedservice.service_apis.question import Question
from feedservice.service_apis.topic import Topic
from feedservice.service_apis.upvote import Upvote
from feedservice.service_apis.feeds import Feeds
django.setup()

app = Flask(__name__)

api = Api(app=app, prefix='/feedservice/')

api.add_resource(Question, 'question', 'question/<int:question_id>')
api.add_resource(Answer, 'answer', 'answer/<int:answer_id>')
api.add_resource(Topic, 'topic', 'topic/<int:topic_id>')
api.add_resource(Upvote, 'upvote', 'upvote/<int:upvote_id>')
api.add_resource(Downvote, 'downvote','downvote/<int:downvote_id>')
api.add_resource(Feeds, 'feeds')

if __name__ == "__main__":
        app.run(port=2006, debug=True)
