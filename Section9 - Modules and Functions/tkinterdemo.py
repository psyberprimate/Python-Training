try:
    import tkinter
except ImportError:    
    import Tkinter as tkinter
print(tkinter.TkVersion)
print(tkinter.TclVersion)

#tkinter._test()

### PACK MANAGER###
# mainWindow = tkinter.Tk()

# mainWindow.title("Hello ZA WORLD")
# mainWindow.geometry('640x480+8+400')

# label = tkinter.Label(mainWindow, text="Hello ZA WORLD")
# label.pack(side='top')

# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

# canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', anchor='n')#'top', fill=tkinter.BOTH, expand=True)

# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)

# button1 = tkinter.Button(mainWindow, text="button1")
# button2 = tkinter.Button(mainWindow, text="button2")
# button3 = tkinter.Button(mainWindow, text="button3")

# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')

# mainWindow.mainloop()

### GRID MANAGER ###

mainWindow = tkinter.Tk()

mainWindow.title("Hello ZA WORLD")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text="Hello ZA WORLD")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)

#Configure columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()