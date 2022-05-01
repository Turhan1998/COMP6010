n = input("Enter a positive number > 2: ")
num1 = 1
num2 = 1
fibonacci = 0

print(str(num1))
print(str(num2))

for x in range(3, int(n) + 1):
  fibonacci = num1 + num2
  num1 = num2
  num2 = fibonacci
  print(str(fibonacci))  


