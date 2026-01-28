import tkinter 
from tkinter.ttk import *
from tkinter import *

Window = Tk()
Window.config(bg="#f5d900")
Window.title("table")
Title = tkinter.Label(Window,text = "Mathematical Table",bg="#f5d900")
Caption = tkinter.Label(Window, text= "Number and Range",bg="#f5d900")
Title.grid(row = 0, column = 0, columnspan=3, pady=25)
Caption.grid(row = 1, column = 0, padx= 10)

Var1 = IntVar()
Numbers = Combobox(Window, textvariable=Var1, width=5)
Numbers['values']=tuple(range(101))
Radiovar = IntVar()
R10 = tkinter.Radiobutton(Window, text = '10', variable=Radiovar, value=10,bg="#f5d900")
R20 = tkinter.Radiobutton(Window, text = '20', variable=Radiovar, value=20,bg="#f5d900")
R30 = tkinter.Radiobutton(Window, text = '30', variable=Radiovar, value=30,bg="#f5d900")
Radiovar.set(10)
Numbers.grid(column=1, row=1)
R10.grid(column=2,row=1)
R20.grid(column=2,row=2, padx = 30)
R30.grid(column=2,row=3, padx = 30)

def Multiplication_Table():
    Tables = ''
    for i in range(Radiovar.get()+1):
        Tables += str(Var1.get())+" X "+str(i)+" = "+str(Var1.get()*i)+"\n"
    table.configure(text =Tables)   

Btn1 = tkinter.Button(Window, text="Generate",command = Multiplication_Table,bg="#f5d900")
table = tkinter.Label(Window,anchor=CENTER,bg="#f5d900")
Btn1.grid(row=4, column=1)
table.grid(row=5, column=1, pady= 25)
Window.mainloop()