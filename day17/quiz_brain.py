
# todo: Asking the questions
# todo: Checking if the answer was correct
# todo: Checking if we are the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        print(f'Your final score is: {self.score}')
        return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # print(current_question.text, current_question.answer)
        self.question_number += 1
        answer = input(f'Q. {self.question_number}: {current_question.text} (True/False)? ')
        self.check_answer(answer, current_question.answer)
        # return answer

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it correct')
            print(f'Your score is: {self.score}')
        else:
            print('Nap, that was not correct.')
        print(f'The correct answer was {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print(f'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')