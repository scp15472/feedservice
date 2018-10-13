from feedservice.db.feed_modules.models import Topic

def update_question(question_object,data):
    if 'string' in data:
        question_object.string= data['string']

    if 'topicId' in data:
        try:
            topic_object = Topic.objects.get(topic_id = data['topicId'])
        except Exception as e:
            print e
            raise e
        question_object.topic = topic_object

    question_object.save()
    return question_object