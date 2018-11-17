from flask_restful import Resource

from feedservice.service_api_handler import question_get_handler
from feedservice.utils.feed_method import get_feed_dict


class Feeds(Resource):
    def get(self):
        questions = question_get_handler.get_question_by_filter({})
        if questions:
            feeds = [get_feed_dict(question) for question in questions]
            return {"feeds": feeds}
        else:
            return {'message': 'There is no feeds!!!'}
