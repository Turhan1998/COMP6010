#Input two integers a and b, output 1 if a is more than b, -1 if a is less than b, 0 if they have the same value.

a = int(input("a= "))
b = int(input("b= "))
if a > b:
  print(str(a) + " is more than " + str(b), ",", "Output = 1")
else:
  if a < b:
    print(str(a) + " is less than " + str(b), ",", "Output = -1")
  else:
    print(str(a) + " equals " + str(b), ",", "Output = 0")
