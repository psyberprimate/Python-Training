import point
import turtle

class GuiPoint(point.Point):
    
    def draw(self, canvas, size = 5, color = 'red'):
        
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)