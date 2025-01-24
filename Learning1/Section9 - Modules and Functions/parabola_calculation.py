import math


try:
    import tkinter
except ImportError:
    print("Cannot import tkinter")    


def parabola(canvas : tkinter.Canvas, size: int = '')-> float:
    """_summary_

    Plots are parabola in range +-size with tkinter.Canvas

    Args:
        x (int, optional): _description_. Defaults to ''.

    Returns:
        float: _description_
    """    
    for x in range(size):
        x /= 100
        y = x * x / size
        plot(canvas, x, y)
        plot(canvas, -x, y)

#Modify a circle function that it allows the colour of the circle to be specified and defaults to the color 'red'
def circle(canvas : tkinter.Canvas, radius, g, h, color='red') -> None:
    canvas.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)
    # for x in range(g, g + radius):
    #     y = h + (math.sqrt(radius **2 - ((x-g) ** 2)))
    #     plot(canvas, x, y)
    #     plot(canvas, x, 2*h-y)
    #     plot(canvas, 2 * g - x, y)
    #     plot(canvas, 2 * g - x, 2 * h - y)


def draw_axes(canvas : tkinter.Canvas) -> None:
    """_summary_
    Creates a new center in the middle of the screen
    Args:
        canvas (_type_): _description_
    """    
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(x_origin, 0, -x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(canvas : tkinter.Canvas, x, y) -> tkinter.Canvas:
    """_summary_
    Creates a line
    Args:
        canvas (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        tkinter.Canvas: _description_
    """    
    canvas.create_line(x, -y, x + 1, -y + 1, fill="red")

mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('1980x1080')

canvas = tkinter.Canvas(mainWindow, width=1980, height=1080)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
parabola(canvas, 400)
    
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100, 'blue')
circle(canvas, 100, -100, 100, 'black')
circle(canvas, 100, -100, -100, 'yellow')
circle(canvas, 10, 30, 30, 'white')
circle(canvas, 10, 30, -30, 'orange')
circle(canvas, 10, -30, 30, 'purple')
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)    
    
mainWindow.mainloop()