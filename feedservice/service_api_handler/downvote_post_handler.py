from feedservice.db.feed_modules.models import Downvote,Answer

def create_downvote(data, username):
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

    downvote_object = Downvote.objects.create(answer=answer_object, username =username)
    return downvote_object