from feedservice.utils.answer_methods import get_answer_feed
from feedservice.utils.question_methods import get_question_dict


def get_feed_dict(question):
    question_response = get_question_dict(question)
    print question.answers.all()
    question_response.update({"answers": [get_answer_feed(answers) for answers in question.answers.all()]})
    return question_response