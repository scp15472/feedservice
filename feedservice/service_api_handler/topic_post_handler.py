from feedservice.db.feed_modules.models import Topic

def create_topic(data):
    try:
        topic_id = data['topic_id']
        name = data['name']
    except Exception as e:
        print e
        raise e

    topic_object = Topic.objects.create(topic_id=topic_id, name=name)
    return topic_object


