"""
## Debug Leap Year

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

- Read this the code in main.py
- Spot the problems 🐞. 
- Modify the code to fix the program. 
- No shortcuts - don't copy-paste to replace the code entirely with a working solution. 

Fix the code so that it works and when you hit submit it should pass all the tests.

# Solution

[https://repl.it/@appbrewery/day-13-2-solution](https://repl.it/@appbrewery/day-13-2-solution)
"""
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  