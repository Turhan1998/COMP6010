sum = 0
average = 0
for number in range(1, 101):
  sum += number
  print(str(number) + "  " + str(sum))
average = sum/100
print("sum = " + str(sum))  
print("average = " + str(average))
  