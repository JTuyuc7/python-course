

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
is_on = True

for item in question_data:
    question_text = item['text']
    question_answer = item['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    # print(item['text'], 'cada item')
    # print(item['answer'])

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
