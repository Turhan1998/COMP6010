import random
num = random.randint(1, 1000)
while num < 1000:
  print(num)
  if num % 3 == 0:
    break
  num = random.randint(1, 1000)
