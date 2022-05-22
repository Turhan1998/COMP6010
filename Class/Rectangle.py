class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # def __init__(self, side):
    #     self.width = side
    #     self.height = side
    
    def __str__(self):
        return str(self.width) +" by "+ str(self.height)


    def __eq__(self, other) :
        '''Return True if the two objects are equal based on their hape
    5 by 8 equals 5 by 8
    5 by 8 equals 8 by 5
    5 by 8 does NOT equals 2 by 20 '''
        if self.width == other.width and self.height == other.height:
            return True
        if self.width == other.width and self.height == other.width:
            return True
        return False
#r = Rectangle(20)
#print(r.width, r.height)

s = Rectangle(20,80)
print(s.width, s.height)
print("String value is : ", str(s))

r = Rectangle(20,30)
print(r==s)

