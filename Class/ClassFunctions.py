class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height


    def __eq__(self, other):
        if self.area == other.area:
            return True
        return False

r = Rectangle(20,40)
s = Rectangle(4,4)

print(r.width, r.height)

print(r.area())
print(r.is_square())

print(s.area())
print(s.is_square())


print(r == s)



















