from random import randint

def roll_dice(number,sides):
  total = 0
  for _ in range(number):
    total += randint(1, sides)
  return total