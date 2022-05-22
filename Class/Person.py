class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p = Person("Turhan", 24, "Female")
husband = p
print(p.name, p.age, p.gender)
print(husband.name)
