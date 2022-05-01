num = input("Enter a positive number: ")
factorial = 1
for x in range(1, int(num)+1):
  factorial *= x
  print(str(x) + "! = " + str(factorial))  


n = int(input("Enter positive num: "))
fact = 1

for i in range(1, n + 1):
      fact = fact *i
      print(str(i) + "! = " + str(fact))
