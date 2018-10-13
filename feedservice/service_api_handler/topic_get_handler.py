from feedservice.db.feed_modules.models import Topic


def get_single_topic(topic_id):
    try:
        topic_object = Topic.objects.get(topic_id=topic_id)
        return topic_object
    except Exception as e:
        print e
        return None


def get_all_topic():
    return Topic.objects.all()
