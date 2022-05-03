from multiprocessing.sharedctypes import Value
import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b): return a / b


print(logo)
res = 0
is_new_calculation = True

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div,
}

while True:
    if is_new_calculation:
        while True:
          try:
            fn = float(input("What is the first number?: "))
          except ValueError:
            print("Invalid input. Please type a number.")
          else:
            break
    else:
        fn = res
    
    while True:
      try:
        op = input("+\n-\n*\n/\nPick an operation: ")
        if op not in operations.key():
          raise ValueError("Invalid operation")
      except ValueError:
        print(f"The operator {op} is not valid. Choose among the listed operations.")
      else:
        break

    while True:
      try:
        ln = float(input("What is the second number?: "))
      except ValueError:
        print("Invalid input. Please type a number.")
      else:
        break
    
    res = operations[op](fn, ln)

    is_new_calculation = input(
        f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ").lower() == 'n'
    if is_new_calculation:
        os.system("clear") if os.name == "posix" else os.system("cls")
