

from random import randint

import point
import rectangle



if __name__ == "__main__":
    
    print("Give coordinates inside the rectangle!")
    
    rectangle_answer = rectangle.Rectangle(point.Point(randint(0, 9), randint(0, 9)),
                                            point.Point(randint(10, 20), randint(10, 20)))
    
    print("Rectangle Coordinates: ",
          "x1: ", rectangle_answer.point1.x, ",",
          "y1: ", rectangle_answer.point1.y, "and",
          "x2: ",rectangle_answer.point2.x, ",",
          "y2: ",rectangle_answer.point2.y
          )
    
    user_point = point.Point(float(input("Guess X: ")),
                             float(input("Guess Y: "))
                             )
    
    print("Your point was inside the rectangle: ",user_point.inside_rectangle(rectangle_answer))
    
    print("Now guess the area of the rectangle!")
    
    user_guess = float(input("Guess area of rectangle: "))
    
    if rectangle_answer.area() == user_guess:
        print("You guessed correct the area of the rectangle is : {}".format(rectangle_answer.area()))
    else:
        print("You guess the rectangle area off by: {}".format(int(rectangle_answer.area() - user_guess)))
        
    