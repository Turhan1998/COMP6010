def my_function(units):
  for x in units:
    print(x)
  return units

myUnits = ["COMP6010", "COMP6200"]
unitCopy = my_function(myUnits)
print(unitCopy)