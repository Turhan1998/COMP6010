number = int(input("Enter an integer between 1 and 100: "))

numOfFactors = 0

for factor in range(1, number+1):
  if number % factor == 0:
    numOfFactors += 1
if numOfFactors == 2:
  print(str(number) + " is a prime.")
else:
  print(str(number) + " is NOT a prime.")
