import tkinter
import os

def reset_calc() -> None:
    global data
    print("reset all")
    data = ''
    print(f"operations are now: {data}")


def reset_operation() -> None:
    global data
    print("reset operation")
    data = data[:-1]
    print(f"new string is: {data}")
    data = ''


def add_number(number : int) -> None: #def add_number(string: str = '',number : int = 0) -> None: 
    global data
    data += str(number)
    print(f"Data is now: {data}")


def add() -> None:
    global data
    print("Add")
    if data[-1] != '+' or '-' or '*' or '/':
        data += "+"
    print(data)

def substract() -> None:
    global data
    print("Subs")
    if data[-1] != '+' or '-' or '*' or '/':
        data += "-"
    print(data)

def multiply() -> None:
    global data
    print("Mul")
    if data[-1] != '+' or '-' or '*' or '/':
        data += "*"
    print(data)

def divide() -> None:
    global data
    print("Div")
    if data[-1] != '+' or '-' or '*' or '/':
        data += "/"
    print(data)


def calc_result() -> None:
    global result
    global data
    string = ''
    result = 0
    for i in range(0,len(data)):
        if data[i] == '+':
            for j in range(i+1, len(data)-i):
                if data[j] != '+' or '-' or '*' or '/':
                    string += str(data[i])   
                    print(string)       
                result += int(string)
                i += j
            continue
        elif data[i] == '-':
            for j in range(i+1, len(data)-i):
                if data[j] != '+' or '-' or '*' or '/':
                    string += str(data[i])     
                result -= int(string)
                i += j
            continue
        elif data[i] == '*':
            for j in range(i+1, len(data)-i):
                if data[j] != '+' or '-' or '*' or '/':
                    string += str(data[i])     
                result *= int(string)
                i += j
            continue
        elif data[i] == '/':
            for j in range(i+1, len(data)-i):
                if data[j] != '+' or '-' or '*' or '/':
                    string += str(data[i])     
                result /= int(string)
                i += j
            continue
        else:
            values = str(result)+data[i]
            result = int(values)  
    data = str(result)             
    print(result)


mainWindow = tkinter.Tk()



mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)

resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=0, column= 0, columnspan=1, rowspan = 1, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=1, column=0, columnspan=1, rowspan = 1, sticky='nw')


#Button
#Reset buttons
CButton = tkinter.Button(mainWindow, text='C', command=reset_calc)
CEButton = tkinter.Button(mainWindow, text='CE', command=reset_operation)
#
CButton.grid(row=1, column=0, columnspan=1, rowspan = 1, sticky=tkinter.E + tkinter.W)
CEButton.grid(row=1, column=1, columnspan=1, rowspan = 1, sticky=tkinter.E + tkinter.W)
#Value buttons
Button1 = tkinter.Button(mainWindow, text='1', command= lambda : add_number(1))
Button2 = tkinter.Button(mainWindow, text='2', command= lambda : add_number(2))
Button3 = tkinter.Button(mainWindow, text='3', command= lambda : add_number(3))
Button4 = tkinter.Button(mainWindow, text='4', command= lambda : add_number(4))
Button5 = tkinter.Button(mainWindow, text='5', command= lambda : add_number(5))
Button6 = tkinter.Button(mainWindow, text='6', command= lambda : add_number(6))
Button7 = tkinter.Button(mainWindow, text='7', command= lambda : add_number(7))
Button8 = tkinter.Button(mainWindow, text='8', command= lambda : add_number(8))
Button9 = tkinter.Button(mainWindow, text='9', command= lambda : add_number(9))
Button0 = tkinter.Button(mainWindow, text='0', command= lambda : add_number(0))
#
Button1.grid(row=4, column=0, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button2.grid(row=4, column=1, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button3.grid(row=4, column=2, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button4.grid(row=3, column=0, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button5.grid(row=3, column=1, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button6.grid(row=3, column=2, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button7.grid(row=2, column=0, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button8.grid(row=2, column=1, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button9.grid(row=2, column=2, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
Button0.grid(row=5, column=0, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)

#Operations
ResultButton = tkinter.Button(mainWindow, text='=', command=calc_result)
AddButton = tkinter.Button(mainWindow, text='+', command=add)
SubstractButton = tkinter.Button(mainWindow, text='-', command=substract)
MultiplyButton = tkinter.Button(mainWindow, text='*', command=multiply)
DivideButton = tkinter.Button(mainWindow, text='/', command=divide)
#
ResultButton.grid(row=5, column=1, columnspan=1, rowspan = 1, sticky=tkinter.E + tkinter.W)
AddButton.grid(row=2, column=3, columnspan=1, rowspan = 1, sticky=tkinter.E + tkinter.W)
SubstractButton.grid(row=3, column=3, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
MultiplyButton.grid(row=4, column = 3, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)
DivideButton.grid(row=5, column = 3, columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)

#Exit button
cancelButton = tkinter.Button(mainWindow, text='Exit', command=mainWindow.destroy)
cancelButton.grid(row=0, column=1,columnspan=1, rowspan = 1, sticky =tkinter.E + tkinter.W)

result = 0
data = ''
operations = []
numbers = []

mainWindow.update()
mainWindow.mainloop()

#print(rbValue.get())