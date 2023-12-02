class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
    def check_answer(self, guess):
        return guess.lower() == self.answer.lower()