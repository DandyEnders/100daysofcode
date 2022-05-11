from question_model import Question
from data import question_data

question_bank = [Question(t, a) for t, a in question_data]
print(question_bank)
