# calculator
import rng, sys, json
calculator_history = [] 

# creates a new history file if it dosent
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
  return a / b

# temperature conversion
def conversions():
  while True:
    try:
      choice = input("1(Celsius to fahrenheit), 2(Fahrenheit to celsius),\n3(back)?: ")
      match choice:
        case "1":
          celsius = float(input("Celsius: "))
          fahrenheit = (celsius * 1.8) + 32
          print(f"{celsius}°C = {fahrenheit}°F")

        case "2":
          fahrenheit = float(input("Fahrenheit: "))
          celsius = (fahrenheit - 32) / 1.8
          print(f"{fahrenheit}°F = {celsius}°C")

        case "3":
          break

        case _:
          raise ValueError
    except(ValueError):
      print("Invalid input.")
      continue


def sub_menu(calculator_history):
  while True:
    try:
      menu = int(input("1(view) or 2(clear history), 3(rng), 4(conversions)\n5(quit), or 6(back)?:"))
      match menu:
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

# conversions
        case 4:
          conversions()

# quit
        case 5:
          sys.exit()

# goes back to main menu
        case 6:
          break

        case _:
          raise ValueError
    except(ValueError):
      print("Invalid input.")
      continue

def main_menu(calculator_history):
  while True:
    operation_select = int(input("1(add), 2(sub), 3(mult), 4(div), or 5(sub menu)?:"))
# checks if the input isnt 5, else sub menu
    if operation_select == 5: 
      sub_menu(calculator_history)
    else: break
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
    operation_select = main_menu(calculator_history)
    if operation_select not in operations:
      raise ValueError

# number inputs
    num1 = float(input("Enter 1st number:"))
    num2 = float(input("Enter 2nd number:"))

# 1
# matches the operator chosen with operation dict
# then passes the numbers to the function chosen
    operator, calculation = operations[operation_select]
    result = calculation(num1, num2)
    if result.is_integer(): result = int(result)
    if num1.is_integer(): num1 = int(num1)
    if num2.is_integer(): num2 = int(num2)
    print(f"{num1} {operator} {num2} equals {result}")

# history, writes to list and copies it to storage.json
    calculator_history.append({
    "calculation": f"{num1} {operator} {num2}",
    "result": result
    })
    with open("storage.json", 'w') as f:
      json.dump(calculator_history, f, indent=2) 
  except(ValueError):
    print("Invalid input.")    num2 = float(input("Enter 2nd number:"))

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
