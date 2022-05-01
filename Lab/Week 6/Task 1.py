#1. Write a program to extract the digit of order k of the number n.
# Example: if n is 65498745 and k = 3 your algorithm should output 8.
# Indeed the digit of order 0 is 5, the digit of order 1 is 4, the digit of order 2 is 7 and so on.

number = int(input("Enter positive number: "))

order_k = int(input("Enter an integer: "))
i = 1
result = 0
while (i<= order_k):
    number = number // 10
    i = i+1
number = number % 10
print("The digit is: ", +number)

