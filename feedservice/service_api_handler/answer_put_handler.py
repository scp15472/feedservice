from feedservice.db.feed_modules.models import Question

def update_answer(answer_object,data):
    if 'string' in data:
        answer_object.string= data['string']

    if 'question' in data:
        try:
            question_object = Question.objects.get(question = data['question'])
        except Exception as e:
            print e
            raise e
        answer_object.question = question_object

    answer_object.save()
    return answer_object
