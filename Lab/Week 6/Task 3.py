#3. Write a program to output all prime numbers between 1 and 100. 

num1 = int(input("Enter one number: "))
num2 = int(input("Enter another number: "))

for i in range(num1, num2):
    prime = True
    for j in range(2,i):
        if(i%j == 0):
            prime = False
    if prime == True:
        print (i)

print() 

#Another way

print("Prime numbers are: ")
for number in range(1, 101):
    countFactors =0
    for f in range(1, number + 1):
        if number % f == 0:
            countFactors += 1
    if countFactors ==2:
        print(str(number))
    
    
