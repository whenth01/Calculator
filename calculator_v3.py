session_history = []
import rng
def add(a,b):
  return a + b
def sub(a,b):
  return a - b
def mul(a,b):
  return a * b
def div(a,b):
  if b == 0:
    print("Cannot divide by 0!")
    return None
  return a / b
operations = {
1: ('+', add),
2: ('-', sub),
3: ('*', mul),
4: ('/', div)
}
while True:
  try:
    input0 = int(input("1(add), 2(sub), 3(mult), 4(div) or 5(rng)?:"))
  except:
    print("Invalid input! restarting..")
    continue
  if input0 == 5:
    rng.rng_function()
    continue
  input1 = float(input("Enter a number:"))
  input2 = float(input("Enter a number:"))
  operator, operator_stuff = operations[input0]
  output = operator_stuff(input1, input2)
  if output == None:
    continue
  if output == int(output):
    output = int(output)
  print(f"{input1} {operator} {input2} equals {output}")
  session_history.append({
  "calculation": f"{input1} {operator} {input2}",
  "result": output
  })
  while True:
    input01 = input("Restart, quit, view history or RNG?:")
    if input01.lower() in ("restart", "r", "rest", "1"):
      break
    elif input01.lower() in ("history", "h", "hist", "3"):
      for history in session_history:
        print(f"{history['calculation']} = {history['result']}")
      continue
    elif input01.lower() in ("q", "quit", "stop", "2"):
      exit()
    elif input01.lower() in ("rng", "3", "random"):
      rng.rng_function()
    else:
      print("Invalid input! restarting..")
      continue