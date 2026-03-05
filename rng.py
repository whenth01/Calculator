# rng
import json,random
if __name__ == "__main__":
  print("Run calculator_v3.py for it to work.")

# main function
def rng_function(rng_history):
  while True:
    try:
      choice = int(input("1(continue), 2(view) or 3(clear) RNG history, or 4(back)?:"))
      match choice:

# user inputs for RNG
        case 1:
          num1 = input("Smallest number(default is 1):")
          if num1 == "":
            num1 = 1
          else:
            num1 = int(num1)
          num2 = int(input("Largest number:"))
          if num1 > num2:
            print("Smallest number should be smaller than largest.")
            continue
          dice = int(input("Dice rolls:"))

# history viewer
        case 2:
          for hist in rng_history:
            print(f"{hist['dice']}d {hist['smallest_number']} - {hist['largest_number']} = {hist['results']}")
          if len(rng_history) < 1:
            print("History is empty.")
          continue

# history deletion
        case 3:
          with open("rng_storage.json", 'w') as f:
            json.dump([], f)
          rng_history.clear()
          print("RNG History cleared!")
          continue

# return to calculator
        case 4:
          break


    except ValueError:
      print("Invalid input!")
      continue
    else:
      if dice > 1000 or dice < 1:
        print("Max dice rolls is 1000, minimum is 1.")
        continue
    results = []
    
# number generation
    for i in range(dice):
      num = random.randint(num1,num2)
      results.append(num)
      print(f"{num}")

# history writing
    rng_history.append({
    "largest_number": num2,
    "smallest_number": num1,
    "dice": dice,
    "results": results
    })    
    with open("rng_storage.json", 'w') as f:
      json.dump(rng_history, f, indent=2) 

# what calculator calls to run the rng
def run():
# creates a new history file if it dosent exist
  rng_history = []
  try:
    with open("rng_storage.json", 'r') as f:
      rng_history = json.load(f)
  except (FileNotFoundError,json.JSONDecodeError):
    with open("rng_storage.json", "w") as f:
      json.dump(rng_history, f, indent=2)
  rng_function(rng_history)
