# calculator
import rng, sys, json
calculator_history = []
# creates a new history file if it dosent exist

try:
  with open("storage.json", 'r') as f:
    calculator_history = json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
  with open("storage.json", "w") as f:
    json.dump(calculator_history, f, indent=2) 

# calculation functions
# these are picked by the user
# the code checks which function to call
# this occurs at the comment marked with 1
def add(a,b):
  return a + b
def sub(a,b):
  return a - b
def mul(a,b):
  return a * b
def div(a,b):
  if b == 0:
    raise ZeroDivisionError
  return a / b


def questions(calculator_history):
  while True:
    operation_select = int(input("1(add), 2(sub), 3(mult), 4(div) or 5(etc)?:"))
# checks if the input isnt 5, else sub menu
    if operation_select != 5:
      break
    else:
      while True:
        sub_menu = int(input("1(view) or 2(clear history), 3(rng), 4(quit) or 5(back)?:"))
        match sub_menu:

# history viewer
          case 1:
            for history in calculator_history:
              print(f"{history['calculation']} = {history['result']}")
            if len(calculator_history) < 1:
              print("History is empty.")
            
            

# clears history
          case 2:
            with open("storage.json", 'w') as f:
              json.dump([], f)
            calculator_history.clear()
            print("Cleared.")

# activates the rng function in rng.py
          case 3:
            rng.run()

# quit
          case 4:
            sys.exit()

# goes back to main menu
          case 5:
            break
  return operation_select

# operator dictionary
operations = {
1: ('+', add),
2: ('-', sub),
3: ('*', mul),
4: ('/', div)
}

# the inputs, stuff the user interacts with
while True:
  try:
    operation_select = questions(calculator_history)
  except(ValueError):
    print("Invalid input! restarting..")
    continue
  if operation_select not in operations:
    print("Invalid input!")
    continue

# number inputs
  try:
    num1 = float(input("Enter 1st number:"))
    num2 = float(input("Enter 2nd number:"))

# 1
# matches the operator chosen with operation dict
# then passes the numbers to the function chosen
    operator, calculation = operations[operation_select]
    result = calculation(num1, num2)
  except(ValueError,ZeroDivisionError):
    print("Invalid input! Division by 0 error or letter input.")
    continue
  if result.is_integer(): result = int(result)
  print(f"{num1} {operator} {num2} equals {result}")

# history, writes to list and copies it to storage.json
  calculator_history.append({
  "calculation": f"{num1} {operator} {num2}",
  "result": result
  })
  with open("storage.json", 'w') as f:
    json.dump(calculator_history, f, indent=2) 
