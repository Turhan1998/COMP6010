def isPrime(n):
    if n==1:
        return False
    for i in (2,(int)(math.sqrt(2)) +1):
        if n % i ==0:
            return False
    return True
for number in range(1, 101):
    if (isPrime(number)):
        print(number)

print(isPrime(3))

