

def update_upvote(upvote_object,data):
    if 'is_active' in data:
        upvote_object.is_active = data['is_active']
    upvote_object.save()
    return upvote_object

