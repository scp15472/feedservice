from feedservice.utils.answer_methods import get_answer_dict


def get_upvote_dict(upvote_object):
    response = {"username": upvote_object.username,
                "is_active": upvote_object.is_active,
                "answer": get_answer_dict(upvote_object.answer),
                "createdOn": upvote_object.create_on.strftime('%d,%m,%Y'),
                }
    return response



