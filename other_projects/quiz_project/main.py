from data import question_data
from question_model import Question
from quiz_brain import *

question_bank = []

for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

new_sequence = QuizBrain(question_bank)

while new_sequence.has_question():
    new_sequence.next_question()

print("You've finished the quiz!")
print(f"Your final score is {new_sequence.score}/{new_sequence.question_number}")