from feedservice.db.feed_modules.models import Question

def get_single_question(question_id):
    try:
        question_object = Question.objects.get(id=question_id)
        return question_object
    except Exception as e:
        print e;
        return None

def get_question_by_filter(filters):
    criteria = {}
    if 'topicId' in filters:
        criteria['topic_id']=filters['topicId']
    question_object = Question.objects.filter(**criteria)
