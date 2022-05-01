num1 = 1
num2 = 2
num3 = 0
count = 3
number = int(input("Enter a positive integer >=3: "))
print("1: " + str(num1))
print("2: " + str(num2))
while (count <= number):
  num3 = num1 + num2
  print(str(count) + ": " + str(num3))
  num1 = num2
  num2 = num3
  count = count + 1  

 