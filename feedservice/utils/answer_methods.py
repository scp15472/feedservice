from feedservice.utils.question_methods import get_question_dict


def get_answer_dict(answer_object):
    response = {"string":answer_object.string,
                "id":answer_object.id,
                "username":answer_object.username,
                "question": get_question_dict(answer_object.question),
                "create_On":answer_object.create_on.strftime('%d,%m,%y')}
    return response

def get_answer_feed(answer_object):
    response = {"string":answer_object.string,
                "id":answer_object.id,
                "username":answer_object.username,
                "create_On":answer_object.create_on.strftime('%d,%m,%y'),
                "upvoteCount":answer_object.upvote_set.all().count(),
                "downvoteCount": answer_object.downvote_set.all().count()}
    return response