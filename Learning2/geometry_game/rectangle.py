#class for rectangle

class Rectangle:
    
    
    def __init__(self, point1, point2):
        
        print("__init__")
        self.point1 = point1
        self.point2 = point2
        
        
    def area(self):
        
        return abs((self.point2.x - self.point1.x) * \
                (self.point2.y - self.point1.y))
    
    

