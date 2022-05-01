#4. Assume a 3-digit number can be represented as D2D1D0. There are some numbers where D2D1D0=
#D2^3+ D1^3+D0^3. For instance, 153=1^3+5^3+3^3 (note: 5^3=5*5*5).
#Write a program to output all this kind of 3-digit positive numbers.

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            number = i * 100 + j * 10 + k
            if number == pow(i,3) + pow(j,3)+ pow(k,3):
            #if number = i*i*i + j*j*j + k*k*k:
            #if number = i**3 + j**3 + k**3:
                print(number)
            


