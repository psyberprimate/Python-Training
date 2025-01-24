from canvas import Canvas
from geometric_shapes import Square, Rectangle, Triangle, Circle

def ask_for_input(canvas):
    """
    Ask for user input to the program
    """
    while(True):
        user_input = input("What would you like to draw? Enter quit to quit the program. ")
        match user_input.lower():
            case "square":
                #settings
                x_coord = int(input("Enter x row pixel of the the square (from left top): "))
                y_coord =  int(input("Enter y column pixel of the square: "))
                side = int(input("Enter the side lenght of the square: "))
                #colors
                red = int(input("Enter how much red RGB has: (0-255): "))
                green = int(input("Enter how much green RGB has: (0-255): "))
                blue = int(input("Enter how much blue RGB has: (0-255): "))
                square = Square(x=x_coord, y=y_coord, side = side, colors=(red, green, blue))
                square.draw(picture)
                
            case "rectangle":
                #settings
                x_coord = int(input("Enter x row pixel of the rectangle (from left top): "))
                y_coord =  int(input("Enter y column pixel of the rectangle: "))
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                #colors
                red = int(input("Enter how much red RGB has: (0-255): "))
                green = int(input("Enter how much green RGB has: (0-255): "))
                blue = int(input("Enter how much blue RGB has: (0-255): "))
                rectangle = Rectangle(x=x_coord, y=y_coord, height=height, width=width, colors=(red, green, blue))
                rectangle.draw(picture)
                
            case "triangle":
                #settings
                x_coord = int(input("Enter x row pixel of the triangle: "))
                y_coord =  int(input("Enter y column pixel of the triangle: "))
                base = int(input("Enter the base of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                #colors
                red = int(input("Enter how much red RGB has: (0-255): "))
                green = int(input("Enter how much green RGB has: (0-255): "))
                blue = int(input("Enter how much blue RGB has: (0-255): "))
                triangle = Triangle(x=x_coord, y=y_coord, base=base, height=height, colors=(red, green, blue))
                triangle.draw(picture)
                
            case "circle":
                #settings
                x_coord = int(input("Enter x row pixel of the circle: "))
                y_coord =  int(input("Enter y column pixel of the circle: "))
                radius = int(input("Enter the radius of the circle: "))
                #colors
                red = int(input("Enter how much red RGB has: (0-255): "))
                green = int(input("Enter how much green RGB has: (0-255): "))
                blue = int(input("Enter how much blue RGB has: (0-255): "))
                circle = Circle(x=x_coord, y=y_coord, radius=radius, colors=(red, green, blue))
                circle.draw(picture)
                
            case "quit":
                print("***Exiting program***")
                break
            case _:
                print("***Invalid input***")
        

if __name__ == "__main__":
    
    path = 'math_painter/'
    name = 'modern_art'
    canvas_colors = {"white" : (255, 255, 255), "black" : (0, 0, 0)}
    
    print("*****Math painter version 0*****")
    
    canvas_width = input("Enter the width of the canvas: ")
    canvas_height = input("Enter the height of the canvas: ")
    print("Do you want black or white canvas?")
    user_colors = input("Enter canvas color (white or black): ")
    
    try:
        picture = Canvas(width=canvas_width, height=canvas_height, color=canvas_colors[user_colors])
    except Exception as e:
        print("Wrong canvas provided - error: {}".format(e))
        print("Setting default white canvas")
        picture = Canvas(width=1000, height=1000, color=canvas_colors["white"])
        
    ask_for_input(picture)
    #print .pgn picture
    picture.make(image_path=path, image_name=name) 
    print(f"Image - {name}.png created")