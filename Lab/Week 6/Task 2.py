#2. Write a program to convert a decimal number to a binary. 





decimal = int(input("\nEnter Decimal Number: ",))

result = ""
while decimal > 0:
   if decimal % 2 == 0:
       result = "0" + result 
   else:
        result = "1" + result 
   decimal = decimal//2


print("\nEquivalent Binary Value = ", result)
print()