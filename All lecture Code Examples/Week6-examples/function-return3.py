def my_function1(units):
  for x in units:
    x = x.lower()
    print(x)
  #print(units)
  return units

def my_function2(units):
  for i in range(len(units)):
    units[i] = units[i].lower()
    print(units[i])
  #print(units)
  return units

myUnits = ["COMP6010", "COMP6200"]
unitCopy = my_function1(myUnits)
print(unitCopy)

unitCopy = my_function2(myUnits)
print(unitCopy)