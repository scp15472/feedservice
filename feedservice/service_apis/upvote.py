import django;
from flask import jsonify, request
from flask_restful import Resource

from feedservice.service_api_handler import upvote_post_handler, \
    upvote_get_handler, upvote_put_handler
from feedservice.services.user_service import is_authenticated
from feedservice.utils import upvote_methods

django.setup()


class Upvote(Resource):
    def post(self):
        data = request.get_json()

        token = request.cookies.get('token')
        print token
        status, user_data = is_authenticated(token)
        if not status:
            raise Exception

        upvote_object = upvote_post_handler.create_upvote(data,user_data['username'])
        response = upvote_methods.get_upvote_dict(upvote_object)
        return jsonify({"upvote": response})

    def get(self, upvote_id=None):
        if upvote_id:
            upvote_object = upvote_get_handler.get_single_upvote(upvote_id)
            if upvote_object:
                response_dict = upvote_methods.get_upvote_dict(upvote_object)
                return jsonify({"upvote": response_dict})

        # filters = request.args
        # upvote_objects, count = upvote_get_handler.get_upvote_by_filter(filters)
        # response_dict = [upvote_methods.get_upvote_dict(upvote) for upvote in upvote_objects]
        # return jsonify({"upvote": response_dict, 'count':count})

    def put(self,upvote_id):
        upvote_objects = upvote_get_handler.get_single_upvote(upvote_id)
        if upvote_objects:
            data = request.get_json()
            upvote_objects = upvote_put_handler.update_upvote(upvote_objects,data)
            response_dict = upvote_methods.get_upvote_dict(upvote_objects)
            return jsonify({"upvote":response_dict})
        else:
            return jsonify({"Message": "Upvote not found!!!"})