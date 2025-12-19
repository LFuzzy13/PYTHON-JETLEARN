#importing
from tkinter import *
import time

#window
W=Tk()
W.geometry("270x115")
W.config(bg="#5a6aaa")
W.title("Clock")
W.resizable(False,False)

#functions
def update():
    TIMElabel.config(text=time.strftime("%H:%M:%S %p"))
    DATElabel.config(text=time.strftime("%A, %d %B %Y"))
    W.after(1000, update)


#labels
label1=Label(W,text="Digital Clock",bg="#5a6aaa",fg="#d2dbf7",font=("times new roman", 10, "bold"))
label1.pack()

TIMElabel=Label(W,text=update, bg="#5a6aaa", fg="#ced5ea", font=("times new roman", 20, "bold"))
TIMElabel.pack()

DATElabel=Label(W,text=update, bg="#5a6aaa", fg="#d6dcf0", font=("times new roman", 10, "bold"))
DATElabel.pack()

Btn=Button(W,text="Exit.", bg="#5a6aaa", fg="#8a2020", font=("times new roman",10,"bold"),command=W.destroy)
Btn.pack()
update()
#loop
W.mainloop()