numOdd = 0
numEven = 0
number = 0
number = int(input("Enter a positive integer: "))
while (number >= 1):
  if number % 2 == 0:
    numEven += 1
    print("This is an even number")
  else:
    numOdd += 1
    print("This is an odd number")
  number = int(input("Enter a positive integer: "))
print("There are " + str(numOdd) + " odd numbers")  
print("There are " + str(numEven) + " even numbers")  
