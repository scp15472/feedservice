from feedservice.db.feed_modules.models import Downvote,Answer

def create_downvote(data):
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

    downvote_object = Downvote.objects.create(answer=answer_object, username =user_name)
    return downvote_object