n = int(input("Enter a positive number > 2: "))
num1 = 1
num2 = 2
fibonacci = 0
print(num1)
print(num2)
for x in range(3, n+1 ):
  fibonacci = num1 + num2
  num1 = num2
  num2 = fibonacci
  print(str(fibonacci))  
