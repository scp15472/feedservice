from feedservice.db.feed_modules.models import Upvote,Answer

def create_upvote(data, username):
    try:
        answer_id = data['answer_id']
        username = username
    except Exception as e:
        print e
        raise e
    try:
        answer_object = Answer.objects.get(id=answer_id)
    except Exception as e:
        print e
        raise e

    upvote_object = Upvote.objects.create(answer=answer_object, username=username)
    return upvote_object