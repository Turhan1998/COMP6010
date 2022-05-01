#1. Assume the following interest rates for bank deposit. Write a program to calculate the interest of a given deposit.

deposit = int(input("Enter amount of deposit: "))
interest = 0
rate = 0 
if deposit >=1 and deposit<=1000:
    rate = 1/100
elif deposit >=1001 and deposit<=10000:
    rate = 1.5/100
elif deposit >=10001 and deposit<=50000:
    rate = 1.8/100
elif deposit >=50001 and deposit<=100000:
    rate = 2/100
    
else:
    rate = 2.5/100
interest = "{:.2f}".format(deposit*rate) #formatting whatever in bracket {} in 2 decimal places
print("Interest : ", interest)
