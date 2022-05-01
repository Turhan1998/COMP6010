num = input('Please enter the number: ')

temp = int(num)//10
rem = temp%10
print('The second-last digit is: ', rem)

n = abs(int(num))

while n >= 10:
    n = n//10


print('The first digit is: ', n)


