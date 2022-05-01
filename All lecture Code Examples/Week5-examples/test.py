'''output = ""
a = 26
while a != 1:
    output = output + str(a)
    if a%2 == 0:
        a = a//2
    else:
        a = 3*a + 1
print("output = ", output)
'''

'''output = ""
for i in range(10):
    if i%2 == 0:
        output = output + str(i)
print("Output", output)'''

'''output = ""
for i in range(5):
    output = output + str(i)
print(output)'''


'''a,b = 3,7
output = "hi"
if a//2 == b//3:
    output = output + "2"
else:
    output = output + "3"

print(output)'''


a,b,c,d = 3,7,2,5
output = ""
if a%2 == b%2:
    output = output + "1"
    if d//c != b//a:
        output = output + "2"
    else:
        output = output + "3"
else:
    output = output + "4"
    if d//c != b//a:
        output = output + "5"
    else:
        output = output + "6"
print(output)