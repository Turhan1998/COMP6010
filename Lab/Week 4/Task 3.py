#3. Write a while loop to calculate the sum of all odd numbers between 1 and 100 and the sum of all
#even numbers between 1 and 100, respectively. Write your solution using for loop too.
number = 1
sumOdd = 0
sumEven = 0
print("Using while loop")
while (number <= 100):
  if number % 2 == 1:
    sumOdd += number
  else:
    sumEven += number
  number += 1
print("Sum of odd = " + str(sumOdd))
print("Sum of even = " + str(sumEven))

print()
print("Using for loop")
for i in range(1, number+1 <= 100):
    if number % 2 == 1:
        sumOdd += number
    else:
        sumEven += number

print("Sum of all odd numbers between 1 and 100: ", sumOdd)
print("Sum of all even numbers between 1 and 100: ", sumEven)

# simpler way
s=0
for i in range(1,100+1,2):
    s=s+i
print("The sum of odd no is:", s)
for i in range(0,100+1,2):
    s=s+i
print("The sum of even no is:", s)



for i in range(5,0,-1):
    print("*"*i)