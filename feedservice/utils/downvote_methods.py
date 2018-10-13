from feedservice.utils.answer_methods import get_answer_dict


def get_downvote_dict(downvote_object):
    response = {"username": downvote_object.username,
                "is_active": downvote_object.is_active,
                "answer": get_answer_dict(downvote_object.answer),
                "createdOn": downvote_object.create_on.strftime('%d,%m,%Y'),
                }
    return response




