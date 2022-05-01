number = 1
sum = 0
average = 0
while (number <= 100):
  sum += number
  print(str(number) + "  " + str(sum))
  number += 1
average = sum/100
print("sum = " + str(sum))  
print("average = " + str(average))
  