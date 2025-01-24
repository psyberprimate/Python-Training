import turtle
import gui_rectangle
import gui_point
import point
from random import randint

# myturtle = turtle.Turtle()

# myturtle.penup()
# myturtle.goto(50, 75)
# myturtle.pendown()
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(200)
# myturtle.left(90)
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(200)

# turtle.done()

if __name__ == "__main__":
    
    drawturtle = turtle.Turtle()
    rectangle_answer = gui_rectangle.GuiRectangle(point.Point(randint(0, 400), randint(0, 400)),
                                            point.Point(randint(10, 400), randint(10, 400)))
    
    print("Rectangle Coordinates: ",
          "x1: ", rectangle_answer.point1.x, ",",
          "y1: ", rectangle_answer.point1.y, "and",
          "x2: ",rectangle_answer.point2.x, ",",
          "y2: ",rectangle_answer.point2.y
          )
    
    user_point = gui_point.GuiPoint(float(input("Guess X: ")),
                             float(input("Guess Y: "))
                             )
    
    print("Your point was inside the rectangle: ",user_point.inside_rectangle(rectangle_answer))
    
    print("Now guess the area of the rectangle!")
    
    user_guess = float(input("Guess area of rectangle: "))
    
    if rectangle_answer.area() == user_guess:
        print("You guessed correct the area of the rectangle is : {}".format(rectangle_answer.area()))
    else:
        print("You guess the rectangle area off by: {}".format(int(rectangle_answer.area() - user_guess)))
        
    rectangle_answer.draw(canvas=drawturtle)
    user_point.draw(canvas=drawturtle)
    
    turtle.done()