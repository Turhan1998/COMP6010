# Format - Strings
# example from w3schools
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
print(myorder.format(quantity, itemno, price))
# use index numbers {0} to be sure the arguments are placed in the correct placeholders:
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))