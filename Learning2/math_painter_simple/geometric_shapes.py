



class Square(object):
    """
    Calculate the canvas pixels in range to draw a Square
    """    
    def __init__(self, x : int, y : int, side : int, colors: tuple):
        """
        for clarification x is row, and y is column
        """        
        self.x = x
        self.y = y
        self.side = side
        self.colors = colors
    
    def draw(self, canvas):
        canvas.pixel_data[self.x: self.x+self.side, self.y: self.y+self.side] = self.colors
    
class Rectangle(object):
    """
    Calculate the canvas pixels in range to draw a Rectangle
    """   
    def __init__(self, x : int, y : int, height : int, width : int, colors : tuple):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colors = colors
        
    def draw(self, canvas):
        canvas.pixel_data[self.x:self.x + self.height, self.y:self.y + self.width] = self.colors
  
  
class Triangle(object):
    """
    Calculate the canvas pixels in range to draw triangle from tip to bottom
    """    
    def __init__(self, x : int, y : int, base : int, height : int, colors : tuple):
        self.x = x
        self.y = y
        self.base = base
        self.height = height
        self.colors = colors
        
    def draw(self, canvas):
        for row in range(self.height):
            # To make a sinmple triangle needs start and end point that increase the width with every iteration at an equal rate
            split_tringle_base = int(self.base / 2)
            width_per_iteration = int(row * (self.base / (2 * self.height)))
            starting_point = self.x + split_tringle_base - width_per_iteration
            ending_point = self.x + split_tringle_base + width_per_iteration
            canvas.pixel_data[self.y + row, starting_point:ending_point] = self.colors
    
class Circle(object):
    """
    Calculate the canvas pixels in range to draw a circle centered around point (x, y)
    """    
    def __init__(self, x : int, y : int, radius : int, colors : tuple):
        self.x = x
        self.y = y
        self.radius = radius
        self.colors = colors
        
    def draw(self, canvas):
        # use min to get max possible range for the canvas without the need to iterate over the full canvas if possible
        maximum_width = min(self.x+self.radius, canvas.width) 
        maximum_height = min(self.x+self.radius, canvas.width)
        for i in range(self.x-self.radius, maximum_width):
            for j in range(self.y-self.radius, maximum_height):
                if (i - self.x) ** 2 + (j - self.y) ** 2 <= self.radius ** 2:
                    canvas.pixel_data[j, i] = self.colors
    
    


        