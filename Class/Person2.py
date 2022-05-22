class Date:

    def __init__(self, d, m, y):
        self.day = d
        self.month = m 
        self.year = y



#dob = Date object, so it gives you a referene
#dob is reference of Date class
class Person:
    def __init__(self, name, dob, gender):  
        self.name = name
        self.dob = dob
        self.gender = gender

d = Date(1, 3, 1998)
p = Person("Turhan", d, "Female")
print(p.name, p.dob, p.gender)

