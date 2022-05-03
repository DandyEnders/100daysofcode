student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heights = 0
for height in student_heights:
  sum_heights += height
average_height = sum_heights / len(student_heights)
print(average_height)
