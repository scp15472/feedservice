def update_downvote(downvote_object,data):
    if 'is_active' in data:
        downvote_object.is_active = data['is_active']
    downvote_object.save()
    return downvote_object
