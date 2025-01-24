try:
    import tkinter
except ImportError:
    print("Cannot import tkinter")    


def parabola(x: int = '')-> float:
    """_summary_
    returns y = x * x, a parabola
    Args:
        x (int, optional): _description_. Defaults to ''.

    Returns:
        float: _description_
    """    
    y = x * x
    return y


def draw_axes(canvas):
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
    print(locals())

def plot(canvas, x, y) -> tkinter.Canvas:
    """_summary_
    Creates a line
    Args:
        canvas (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        tkinter.Canvas: _description_
    """    
    canvas.create_line(x, y, x+1, y + 1, fill="red")

mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('1980x1080')

canvas = tkinter.Canvas(mainWindow, width=990, height=540, background = 'green')
canvas.grid(row=0, column=0)


canvas2 = tkinter.Canvas(mainWindow, width=990, height=540, background='blue')
canvas2.grid(row=0, column=1)


print(repr(canvas), repr(canvas2))

draw_axes(canvas)
draw_axes(canvas2)

for i in range(-100, 100):
    y = parabola(i)
    #print(y)
    plot(canvas, i, y)
    
    
mainWindow.mainloop()