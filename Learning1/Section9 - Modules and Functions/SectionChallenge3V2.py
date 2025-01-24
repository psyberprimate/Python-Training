import tkinter
import os


def action():
    print()


mainWindow = tkinter.Tk()

key = [[('C', 1), ('CE', 1)],
       [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
       [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
       [('7', 1), ('8', 1), ('9', 1), ('*', 1)],
       [('0', 1), ('=', 1), ('/', 1)],
       ]

mainWindowPadding = 8
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyrow in key:
    col = 0
    for key in keyrow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W, command=action)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())

mainWindow.mainloop()

#print(rbValue.get())