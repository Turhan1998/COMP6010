factorial = 1
number = int(input("Enter a positive integer: "))
for factor in range(1, number+1):
  factorial = factorial * factor
print(str(number) + "! = " + str(factorial))  
 