from tkinter import *
import random

w=Tk()
w.title("activity picker 1000")
w.geometry("200x200")
w.config(bg="#cbcbcb")

list=["op1","op2","op3","op4","op5"]

lbl=Label(w,text="Press The Button Below!", bg="#9d9d9d", fg="#0e0e0e")
lbl.pack()

lbl2=Label(w,text=".", bg="#9d9d9d", fg="#0e0e0e")
lbl2.place(relx=0.5, rely=0.4, anchor=CENTER)
def RANDY():
    ACT=random.choice(list)
    lbl2.config(text="You Chose "+ACT)
    


btn1=Button(w,bg="#9d9d9d", fg="#0e0e0e", text="Press", command=RANDY)
btn1.place(relx=0.5, rely=0.6, anchor=CENTER)



w.mainloop()