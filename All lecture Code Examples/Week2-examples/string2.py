unitName = "Fudamental of Computer Science"
unitCode = 'COMP6010'
print(unitCode)
print(unitName)
# below is straitforward
print(unitCode + " is " + unitName)


print(unitCode + "is" + unitName)
# alternatively, we use f'' to format the entire string directly, {unitCode} is the value of unitCode
msg = f'{unitCode} is {unitName}'
print(msg)


