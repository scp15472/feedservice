import django;
from flask import jsonify, request
from flask_restful import Resource

from feedservice.service_api_handler import downvote_post_handler, \
    downvote_get_handler, downvote_put_handler
from feedservice.services.user_service import is_authenticated
from feedservice.utils import downvote_methods

django.setup()


class Downvote(Resource):
    def post(self):
        data = request.get_json()

        token = request.cookies.get('token')
        print token
        status, user_data = is_authenticated(token)
        if not status:
            raise Exception

        downvote_object = downvote_post_handler.create_downvote(data,user_data['username'])
        response = downvote_methods.get_downvote_dict(downvote_object)
        return jsonify({"downvote": response})

    def get(self, downvote_id=None):
        if downvote_id:
            downvote_object = downvote_get_handler.get_single_downvote(downvote_id)
            if downvote_object:
                response_dict = downvote_methods.get_downvote_dict(downvote_object)
                return jsonify({"downvote": response_dict})

        filters = request.args
        downvote_objects, count = downvote_get_handler.get_downvote_by_filter(filters)
        response_dict = [downvote_methods.get_downvote_dict(downvote) for downvote in downvote_objects]
        return jsonify({"downvote": response_dict, 'count':count})

    def put(self,downvote_id):
        downvote_objects = downvote_get_handler.get_single_downvote(downvote_id)
        if downvote_objects:
            data = request.get_json()
            downvote_objects = downvote_put_handler.update_downvote(downvote_objects,data)
            response_dict = downvote_methods.get_downvote_dict(downvote_objects)
            return jsonify({"downvote":response_dict})
        else:
            return jsonify({"Message": "Downvote not found!!!"})