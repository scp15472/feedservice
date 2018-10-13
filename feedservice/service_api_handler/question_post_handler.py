from feedservice.db.feed_modules.models import Question,Topic

def create_question(data, username):
    try:
        string = data['string']
        topic_id = data['topicID']
        user_name = data['username']
    except Exception as e:
        print e
        raise e
    try:
        topic_objects = Topic.objects.get(topic_id=topic_id)
    except Exception as e:
        print e
        raise e

    question_object= Question.objects.create(string= string, topic=topic_objects, username =user_name)
    return question_object