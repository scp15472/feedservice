import django;
from flask import jsonify, request
from flask_restful import Resource
from feedservice.service_api_handler import question_post_handler, \
    question_get_handler, question_put_handler
from feedservice.services.user_service import is_authenticated
from feedservice.utils import question_methods

django.setup()


class Question(Resource):
    def post(self):
        data = request.get_json()

        token = request.cookies.get('token')
        print token
        status, user_data = is_authenticated(token)
        if not status:
                raise Exception

        question_object = question_post_handler.create_question(data,user_data['username'])
        response = question_methods.get_question_dict(question_object)
        return jsonify({"question": response})

    def get(self, question_id= None):
        if question_id:
            question_object = question_get_handler.get_single_question(question_id)
            if question_object:
                response_dict = question_methods.get_question_dict(question_object)
                return jsonify({"question": response_dict})

        # filters = request.args
        # question_object = question_get_handler.get_question_by_filter(filters)
        # response_dict = [question_methods.get_question_dict(question) for question in question_object]
        # return jsonify({"questions": response_dict})

    def put(self,question_id):
        question_objects = question_get_handler.get_single_question(question_id)
        if question_objects:
            data = request.get_json()
            question_objects = question_put_handler.update_question(question_objects,data)
            response_dict = question_methods.get_question_dict(question_objects)
            return jsonify({"question":response_dict})
        else:
            return jsonify({"Message": "Question not found!!!"})