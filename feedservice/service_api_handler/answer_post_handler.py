from feedservice.db.feed_modules.models import Answer,Question

def create_answer(data, username):
    try:
        string = data['string']
        question = data['question']
        username = username
    except Exception as e:
        print e
        raise e
    try:
        question_object = Question.objects.get(id=question)
    except Exception as e:
        print e
        raise e

    answer_object= Answer.objects.create(string= string, question=question_object, username=username)
    question_object.answers.add(answer_object)
    return answer_object
