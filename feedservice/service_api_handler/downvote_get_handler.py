from feedservice.db.feed_modules.models import Downvote

def get_downvote_by_filter(filters):
    criteria = {}
    if 'answer' in filters:
        criteria['answer_id'] = filters['answer_id']
    if 'username' in filters:
        criteria['username'] = filters['username']

    downvote_objects = Downvote.objects.filter(**criteria)
    count = downvote_objects.count()
    return downvote_objects, count

def get_single_downvote(downvote_id):
    try:
        downvote_object = Downvote.objects.get(id=downvote_id)
        return downvote_object
    except Exception as e:
        print e
        return None