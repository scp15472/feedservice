from feedservice.utils.question_methods import get_question_dict


def get_answer_dict(answer_object):
    response = {"string":answer_object.string,
                "id":answer_object.id,
                "username":answer_object.username,
                "question": get_question_dict(answer_object.question),
                "create_On":answer_object.create_on.strftime('%d,%m,%y')}
    return response
