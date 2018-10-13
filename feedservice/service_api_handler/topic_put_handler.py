def update_topic(topic_object,data):
    if 'name' in data:
        topic_object.name= data['name']
        topic_object.save()
        return topic_object

