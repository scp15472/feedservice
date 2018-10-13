from feedservice.db.feed_modules.models import Upvote,Answer

def create_upvote(data):
    try:
        answer_id = data['answer_id']
        user_name = data['username']
    except Exception as e:
        print e
        raise e
    try:
        answer_object = Answer.objects.get(id=answer_id)
    except Exception as e:
        print e
        raise e

    upvote_object = Upvote.objects.create(answer=answer_object, username =user_name)
    return upvote_object