class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_number = 0
        self.score = 0

    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        if question.check_answer(input(f"{question.text} True/False: ")):
            self.score += 1
            print("Correct")
        else:
            print("Incorrect")
        
    def has_questions(self):
        return self.q_number < len(self.q_list)