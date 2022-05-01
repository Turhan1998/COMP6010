n = input('Please enter the decimal number: ')
print('Your number is',n)

b= input('Please enter the base to convert to: ')

answer = ''
n = int(n)
b = int(b)
while n > 0:
    r = n % b
    n = n//b
    answer = str(r) + answer

print(f'The answer in base {b} is {answer}')