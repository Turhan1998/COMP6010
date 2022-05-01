#3, Given a positive integer n (say n = 50), use bitwise operators to calculate 100, 200, 25, 12, 6.
n = 50

x1 = n<<1 #100 multiplying by 2
x2 = n<<2 
x3 = n>>1 #25 dividing by 2
x4 = n>>2
x5 = n>>3
print(x1,x2,x3,x4,x5)