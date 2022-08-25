class QuizBrain:

    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            print(f"You have completed the quiz.")
            print(f"You final score is {self.score}/{self.question_no}")

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False)?")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right\n")
        else:
            print("That's wrong!\n")
