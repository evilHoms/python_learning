from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
    
quiz = QuizBrain(question_bank)

while quiz.has_questions():
    quiz.next_question()
    
print(f"You answered all questions, your score is: {quiz.score}")
