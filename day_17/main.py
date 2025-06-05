from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for set in question_data:
    question_bank.append(QuestionModel(set["text"], set["answer"]))

# for item in question_bank:
#     print(item.text)
#     print(item.answer + "\n")


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f'Your final score is {quiz.return_score()}/{quiz.question_number}')