import django;
from flask import jsonify, request
from flask_restful import Resource

from feedservice.service_api_handler import answer_post_handler, answer_get_handler, answer_put_handler
from feedservice.services.user_service import is_authenticated
from feedservice.utils import answer_methods

django.setup()


class Answer(Resource):
    def post(self):
        data = request.get_json()

        token = request.cookies.get('token')
        print token
        status, user_data = is_authenticated(token)
        if not status:
            raise Exception

        answer_object = answer_post_handler.create_answer(data, user_data[
            'username'])
        response = answer_methods.get_answer_dict(answer_object)
        return jsonify({"answer": response})

    def get(self, answer_id= None):
        if answer_id:
            answer_object = answer_get_handler.get_single_answer(answer_id)
            if answer_object:
                response_dict = answer_methods.get_answer_dict(answer_object)
                return jsonify({"answer": response_dict})

        # filters = request.args
        # answer_object = answer_get_handler.get_answer_by_filter(filters)
        # response_dict = [answer_methods.get_answer_dict(answer) for
        #                  answer in answer_object]
        # return jsonify({"answer": response_dict})

    def put(self,answer_id):
        answer_object = answer_get_handler.get_single_answer(answer_id)
        if answer_object:
            data = request.get_json()
            answer_object = answer_put_handler.update_answer(answer_object,data)
            response_dict = answer_methods.get_answer_dict(answer_object)
            return jsonify({"answer" : response_dict})
        else:
            return jsonify({"Message": "Answer not fount!!!"})