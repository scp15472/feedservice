from feedservice.db.feed_modules.models import Answer

def get_single_answer(answer_id):
    try:
        answer_object = Answer.objects.get(id=answer_id)
        return answer_object
    except Exception as e:
        print e
        return None

def get_answer_by_filter(filters):
    criteria = {}
    if 'string' in filters:
        criteria['string']=filters['string']
    answer_object = Answer.objects.filter(**criteria)
    return answer_object
