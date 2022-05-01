unitName = "Fudamental of Computer Science"
unitCode = "COMP6010"
print(len(unitCode))
print(len(unitName))
print("COMP" in unitCode) # True
print("comp" in unitCode) # false, case-sensitive
print("comp" not in unitCode) # True
if "COMP6010" not in unitCode:
  print("This is NOT our unit!")
else:
  print("This is the right unit for us!")


