from feedservice.db.feed_modules.models import Upvote

def get_upvote_by_filter(filters):
    criteria = {}
    if 'answer' in filters:
        criteria['answer_id'] = filters['answer_id']
    if 'username' in filters:
        criteria['username'] = filters['username']
    upvote_objects = Upvote.objects.filter(**criteria)
    count = upvote_objects.count()
    return upvote_objects, count

def get_single_upvote(upvote_id):
    try:
        upvote_object = Upvote.objects.get(id=upvote_id)
        return upvote_object
    except Exception as e:
        print e
        return None