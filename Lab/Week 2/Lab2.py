'''Decimal to Binary and Octal

from unicodedata import decimal
decimal = int(input("Decimal number:"))

binary = bin(decimal)
octal = oct(decimal)
print("Decimal to Binary:", binary)
print("Decimal to Octal:", octal)

'''

'''#3 Last digit of a non negative number
#one way
num = input("Enter number:")
print("The last digit of input is:", num[-1])
#another way
num = int(num)
num = num%10

print("The last digit of input is:", num)
'''


'''#5 Given an integer n, get it is second last digit, and its first digit
n = input("Enter the number: ")
print("The second last digit and first digit are", n[-2], ',', n[0])
'''


'''#6 Given a string, output its first character and last character
n = input("Enter the string: ")
print("First character and last character are", n[0], ',', n[-1])

#anotherway
n=4783474
temp = n//10
rem=temp % 10
print("Second last digit: ", rem)
while temp>=10:
    temp = temp//10
print("First digit: ", temp)
'''


#7 Given a string ‘Hello World’, output the two words separately.
n = input("Enter a string: ")
string = n.split()
for s in string:
    print(s)


n = 'turhan_chy'
n = n.split(_)
print(n[0])
print(n[1])




