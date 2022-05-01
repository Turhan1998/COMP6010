number = int(input("Enter a positive integer between 2 and 100: "))
while (number <2):
  print("Wrong input!")
  number = int(input("Enter a positive integer between 2 and 100: "))
numOfFactors = 2
for factor in range(2, number//2+1):
  if number % factor == 0:
    numOfFactors += 1
if numOfFactors == 2:
  print(str(number) + " is a prime.")
else:
  print(str(number) + " is NOT a prime.")
