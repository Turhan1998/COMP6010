#2. Refer to the tax rates below, write a program to calculate the tax of an income.
income = int(input("Enter amount of tax: "))
rate = 0
tax = 0
if income >=0 and income<=18200:
    tax = 0;
if income >=18201:
    if income<=45000:
        tax = tax + (income-18200)*.19 
    else:
        tax = tax +(45000-18200)*.19
if income >=45001:
    if income<=120000:
        tax = tax + (income-45000)*.325 
    else:
        tax = tax +(12000-45000)*.325
if income >=120001:
    if income<=180000:
        tax = tax + (income-120000)*.37
    else:
        tax = tax +(12000-45000)*.37


if income >=180001:
    
    tax = tax + (income-180000)*.45

print(tax)
    