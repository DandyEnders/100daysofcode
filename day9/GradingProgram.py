student_scores = {
  "Harry": 81,
  "Ran": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for name in student_scores:
  
  grade = ""
  score = student_scores[name]
  if 90 < score <= 100:
    grade = "Outstanding"
  elif 80 < score <= 90:
    grade = "Exceeds Expectations"
  elif 70 < score <= 80:
    grade = "Acceptable"
  else:
    grade = "Fail"
  
  student_grades[name] = grade

print(student_grades)