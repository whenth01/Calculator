rng_history = []
def rng_function():
  loop1 = True
  while loop1:
    try:
      num1 = int(input("Largest number:"))
      dice = int(input("Dice rolls:"))
    except:
      print("Invalid input! only whole numbers are valid.")
      continue
    results = []
    import random
    for i in range(dice):
      num = random.randint(1,num1)
      results.append(num)
      print(f"{num}")
    rng_history.append({
    "amount_rolled": num1,
    "dice": dice,
    "results": results
    })    
    while True:
      question = int(input("Restart rng(1), view rng history(2), or quit(3)?:"))
      if question == 1:
        break
      elif question == 2:
        for rng in rng_history:
          print(f"{rng['dice']}d{rng['amount_rolled']} = {rng['results']}")
        continue
      elif question == 3:
        loop1 = False
        break
      else:
        print("Invalid. Please input a valid entry.")
        continue