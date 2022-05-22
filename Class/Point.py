class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x **2 + self.y ** 2) **0.5


    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return (dx **2 + dy ** 2) **0.5


    def __eq__(self, other): # used when you compare object1 == object2
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self): #called when you display str(object)
        return "("+str(self.x)+", "+str(self.y)+")"



p = Point(10,20)
q = Point(3,4)
r = Point(40,30)
print(p.distance_from_origin())
print(q.distance_from(p))  ###Revise

print("p same as q ?", p==q)
print("q same as r ?", q==r)