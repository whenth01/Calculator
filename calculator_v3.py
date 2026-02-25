import json
import rng
calculator_history = []
with open("storage.json", 'r') as f:
  calculator_history = json.load(f)
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
def history():
  for history in calculator_history:
    print(f"{history['calculation']} = {history['result']}")
def questions():
  global input0
  question = True
  while True:
    input0 = int(input("1(add), 2(sub), 3(mult), 4(div) or 5(etc)?:"))
    if input0 != 5:
      break
    elif input0 == 5:
      while question:
        input0 = int(input("1(view) or 2(clear history), 3(rng), 4(quit) or 5(back)?:"))
        match input0:
          case 1:
            history()
          case 2:
            global calculator_history
            with open("storage.json", 'w') as f:
              json.dump([], f)
            calculator_history = []
            print("Cleared.")
          case 3:
            rng.rng_function()
          case 4:
            exit()
          case 5:
            break       
operations = {
1: ('+', add),
2: ('-', sub),
3: ('*', mul),
4: ('/', div)
}
while True:
  try:
    questions()
  except ValueError:
    print("Invalid input! restarting..")
    continue
  if input0 > 5 or input0 < 1:
    print("Invalid input!")
    continue
  try:
    input1 = float(input("Enter a number:"))
    input2 = float(input("Enter a number:"))
    operator, operator_stuff = operations[input0]
    output = operator_stuff(input1, input2)
  except(ValueError,ZeroDivisionError):
    print("Invalid input! Division by 0 error or letter input.")
    continue
  if output == int(output):
    output = int(output)
  print(f"{input1} {operator} {input2} equals {output}")
  calculator_history.append({
  "calculation": f"{input1} {operator} {input2}",
  "result": output
  })
  with open("storage.json", 'w') as f:
    json.dump(calculator_history, f, indent=2) 
