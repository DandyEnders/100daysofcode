student_scores = input("Input a list of students score: ")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

maximum_score = -999
for ss in student_scores:
  if ss > maximum_score:
    maximum_score = ss
print(maximum_score)

