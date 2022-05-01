mark = int(input("Enter your mark in [0,100]: "))
grade = ''
if mark >= 85:
  grade = "HD"
elif mark >= 75:
  grade = "Distinction"
elif mark >= 65:
  grade = "Credit"
elif mark >= 50:
  grade = "Pass"
else:
  grade = "Fail"
print("Your mark is " + str(mark))
print("Your grade is " + grade)


mark = int(input("Enter mark: "))
grade = ""
if mark>= 85:
  grade = "HD"
elif mark >= 75:
  grade = "Distinction"
elif mark >= 65:
  grade = "Credit"
elif mark >= 50:
  grade = "Pass"
else: 
  grade = "Fail"

print("Your mark is: " + str(mark))
print("Your grade is: " + grade)
  