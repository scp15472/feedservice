from feedservice.db.feed_modules.models import Answer,Question

def create_answer(data):
    try:
        string = data['string']
        question = data['question']
        user_name = data['username']
    except Exception as e:
        print e
        raise e
    try:
        question_object = Question.objects.get(id=question)
    except Exception as e:
        print e
        raise e

    answer_object= Answer.objects.create(string= string, question=question_object, username=user_name)
    return answer_object
