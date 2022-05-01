number = 1
sumOdd = 0
sumEven = 0
while (number <= 10):
  if number % 2 == 1:
    sumOdd += number
    
  else:
    sumEven += number
  number += 1
print("sum of odd = " + str(sumOdd))
print("sum of even = " + str(sumEven))
