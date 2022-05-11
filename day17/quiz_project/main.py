from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q["text"], q["answer"]) for q in question_data]
print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()
