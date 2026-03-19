# calculator
import rng, sys, json, math 

#### HISTORY ####

# creates a new history file if it dosent exist
calculator_history = []
try:
  with open("storage.json", 'r') as f:
    calculator_history = json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
  with open("storage.json", "w") as f:
    json.dump(calculator_history, f, indent=2) 

#### MAIN CALCULATOR FUNCTIONS ####

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
def exp(a,b):
  return a ** b

#### PERCENT FUNCTIONS ####

def add_percent(num1, percentage):
  return num1 + (num1 * percentage)
def sub_percent(num1, percentage):
  return num1 - (num1 * percentage) 


#### ADVANCED MATH FUNCTIONS ####

def sqrt(a):
  return math.sqrt(a)
def cos(a):
  return math.cos(math.radians(a))
def sin(a):
  return math.sin(math.radians(a))
def tan(a):
  return math.tan(math.radians(a))
def acos(a):
  return math.acos(a)
def asin(a):
  return math.asin(a)
def atan(a):
  return math.atan(a)
def nat_log(a):
  return math.log(a)
def b10_log(a):
  return math.log10(a)


#### CONVERSION FUNCTIONS ####

def c_to_f(a):
  return (a * 1.8) + 32
def f_to_c(a):
  return (a - 32) / 1.8
def mi_to_km(a):
  return a * 1.609344
def km_to_mi(a):
  return a * 0.6213711922
def m_to_ft(a):
  return a * 3.28084
def ft_to_m(a):
  return a * 0.3048
def cm_to_in(a):
  return a * 0.3937008
def in_to_cm(a):
  return a * 2.54

#### HISTORY FUNCTION ####

def history(calculator_history):
  with open("storage.json", 'w') as f:
    json.dump(calculator_history, f, indent=2)

#### DICTIONARIES ####
main_operations = {
1: ('+', add),
2: ('-', sub),
3: ('*', mul),
4: ('/', div),
5: ('**', exp)
}

percent_operations = {
2: ('+', add_percent),
3: ('-', sub_percent),
4: ('*', mul),
5: ('/', div)
}

conversion_operations = {
1: ('celsius', 'fahrenheit', c_to_f),
2: ('fahrenheit', 'celsius', f_to_c),
3: ('mile(s)', 'kilometer(s)', mi_to_km),
4: ('kilometer(s)', 'mile(s)', km_to_mi),
5: ('meter(s)', 'foot', m_to_ft),
6: ('foot', 'meter(s)', ft_to_m),
7: ('centimeter(s)', 'inch(es)', cm_to_in),
8: ('inch(es)', 'centimeter(s)', in_to_cm)
}

advanced_math_operations = {
2: ('sqrt', sqrt),
3: ('cos', cos),
4: ('sin', sin),
5: ('tan', tan),
6: ('acos', acos),
7: ('asin', asin),
8: ('atan', atan),
9: ('nat log', nat_log),
10: ('b10 log', b10_log)
} 


#### CONVERSIONS ####
def conversions():
  while True:
    try:
      operation_select = int(input("""\n1) celcius to fahrenheit
2) fahrenheit to Celsius
3) mile to kilometer
4) kilometer to mile
5) meter to foot
6) foot to meter
7) centimeter to inch
8) inch to centimeter
9) back
>>> """))
      if operation_select in range(1, 9):
        name, name2, function = conversion_operations[operation_select]
        num1 = float(input(f"{name}: "))
        result = function(num1)
        if num1.is_integer():
          num1 = int(num1)
        print(f"\n{num1} {name} to {name2} = {result} {name2}")
        continue

      if operation_select == 9: break

      else: raise ValueError

    except(ValueError):
      print("Invalid input.")
      continue


#### ALGEBRA ####
def advanced_math(calculator_history):
  while True:
    try:
      operation_select = int(input("""\n1) back
2) square root of x
3) cosine of x
4) sine of x
5) tangent of x
6) arc cosine of x
7) arc sine of x
8) arc tangent of x
9) natural logarithm of x
10) base-10 logarithm of x
>>>"""))

      if operation_select == 1:
        break

      elif operation_select in range(2, 11):
        name, function = advanced_math_operations[operation_select]
        num1 = float(input(f"{name} of: "))
        result = function(num1)
        print(f"\n{name}({num1}) = {result}")

      else:
        raise ValueError

    except(ValueError):
      print("Invalid input.")
      continue

    calculator_history.append({
    "calculation": f"{name}({num1})",
    "result": result
    })
    history(calculator_history)


#### PERCENTAGES ####
def percent(calculator_history):
  while True:
    try:
      operation_select = int(input("""\n1) back
2) x + y%
3) x - y%
4) x * y%
5) x / y%
>>> """))
      if operation_select == 1:
        break
      if operation_select not in percent_operations:
        raise ValueError

      num1 = float(input("Enter 1st number:"))
      num2 = float(input("Enter 2nd number:"))
      percentage = num2 / 100

      operator, calculation = percent_operations[operation_select]
      result = calculation(num1, percentage)
      print(f"\n{num1} {operator} {num2}% = {result}")

      calculator_history.append({
      "calculation": f"{num1} {operator} {num2}%",
      "result": result
      })
      history(calculator_history)
    except(ValueError):
      print("Invalid input.")
      continue

#### SUB MENU ####
def sub_menu(calculator_history):
  while True:
    try:
      menu = int(input("""\n1) view history
2) clear history
3) rng
4) conversions
5) quit
6) back
>>> """))
      match menu:
# history viewer
        case 1:
          for history_print in calculator_history:
            print(f"{history_print['calculation']} = {history_print['result']}")
          if len(calculator_history) < 1:
            print("History is empty.")       


# clears history
        case 2:
          with open("storage.json", 'w') as f:
            json.dump([], f)
          calculator_history.clear()
          print("Cleared.")

        case 3:
          rng.run()

        case 4:
          conversions()

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

#### MAIN MENU ####
def main_menu(calculator_history):
  while True:
    operation_select = int(input("""\n1) add
2) subtract
3) multiply
4) divide
5) exponent
6) percentages
7) advanced math
8) sub menu
>>> """))

    if operation_select == 6:
      percent(calculator_history)
    elif operation_select == 7: 
      advanced_math(calculator_history)
    elif operation_select == 8:
      sub_menu(calculator_history)
    else: break
  return operation_select


# the inputs, stuff the user interacts with
while True:
  try:
    operation_select = main_menu(calculator_history)
    if operation_select not in main_operations:
      raise ValueError

# number inputs
    num1 = float(input("Enter 1st number:"))
    num2 = float(input("Enter 2nd number:"))

# 1
# unpacks operater dictionary and matches with operation_select
# then passes the numbers to the function chosen
    operator, calculation = main_operations[operation_select]
    result = calculation(num1, num2)
    if result.is_integer(): result = int(result)
    if num1.is_integer(): num1 = int(num1)
    if num2.is_integer(): num2 = int(num2)
    print(f"\n{num1} {operator} {num2} equals {result}")

# history, writes to list and copies it to storage.json
    calculator_history.append({
    "calculation": f"{num1} {operator} {num2}",
    "result": result
    })
    history(calculator_history) 
  except(ValueError):
    print("Invalid input.")
  except(ZeroDivisionError):
    print("Cannot divide by 0!")
