import json
import random
rng_history = []
with open("rng_storage.json", 'r') as f:
  rng_history = json.load(f)
def rng_function():
  loop1 = True
  while loop1:
    try:
      question = int(input("1(continue), 2(view) or 3(clear) RNG history, or 4(back)?:"))
      match question:
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
        case 2:
          global rng_history
          for rng in rng_history:
            print(f"{rng['dice']}d {rng['smallest_number']} - {rng['largest_number']} = {rng['results']}")
          continue
        case 3:
          with open("rng_storage.json", 'w') as f:
            json.dump([], f)
          rng_history = []
          print("RNG History cleared!")
          continue
        case 4:
          loop1 = False
          break
    except ValueError:
      print("Invalid input!")
      continue
    else:
      if dice > 1000:
        print("Max dice rolls is 1000.")
        continue
    results = []
    for i in range(dice):
      num = random.randint(num1,num2)
      results.append(num)
      print(f"{num}")
    rng_history.append({
    "largest_number": num2,
    "smallest_number": num1,
    "dice": dice,
    "results": results
    })    
    with open("rng_storage.json", 'w') as f:
      json.dump(rng_history, f, indent=2) 
