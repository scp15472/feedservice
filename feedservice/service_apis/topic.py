import django;
from flask import jsonify, request
from flask_restful import Resource

from feedservice.service_api_handler import topic_post_handler, \
    topic_get_handler, topic_put_handler
from feedservice.utils import topic_methods

django.setup()


class Topic(Resource):
    def post(self):
        data = request.get_json()
        topic_object = topic_post_handler.create_topic(data)
        response = topic_methods.get_topic_dict(topic_object)
        return jsonify({"topic": response})

    def get(self, topic_id= None):
        if topic_id:
            topic_object = topic_get_handler.get_single_topic(topic_id)
            response_dict = topic_methods.get_topic_dict(topic_object)
            return jsonify({"topic": response_dict})
        else:
            topic_objects = topic_get_handler.get_all_topic()
            response_dict = [topic_methods.get_topic_dict(topic_object) for topic_object in topic_objects]
            return jsonify({"topic": response_dict})


    def put(self,topic_id):
        topic = topic_get_handler.get_single_topic(topic_id)
        if topic:
            data = request.get_json()
            topic_object = topic_put_handler.update_topic(topic,data)
            response_dict = topic_methods.get_topic_dict(topic_object)
            return jsonify({"topic":response_dict})
        else:
            return jsonify({"Message": "topic not found!!!"})