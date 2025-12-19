from tkinter import *
import random

w=Tk()
w.title("Dice Roller")
w.geometry("200x200")
w.config(bg="#db2525")

D6=["6","5","4","3,","2","1"]
D12=["12","11","10","9","8","7","6","5","4","3","2","1"]
D20=["20","19","18","17","16","15","14","13","12","11","10","9","8","7","6","5","4","3","2","1"]



lbl=Label(w,text="Press The Buttons Below!", bg="#9d9d9d", fg="#0e0e0e")
lbl.pack()

d6lbl=Label(w,text=".", bg="#9d9d9d", fg="#ffffff")
d6lbl.place(relx=0.5, rely=0.2, anchor=CENTER)

def D6func():
    ACT=random.choice(D6)
    d6lbl.config(text="You Rolled  "+ACT)
    

btn1=Button(w,bg="#9d9d9d", fg="#0e0e0e", text="D6", command=D6func)
btn1.place(relx=0.5, rely=0.3, anchor=CENTER)

#######################

d12lbl=Label(w,text=".", bg="#9d9d9d", fg="#ffffff")
d12lbl.place(relx=0.5, rely=0.4, anchor=CENTER)

def D12func():
    ACT1=random.choice(D12)
    d12lbl.config(text="You Rolled  "+ACT1)

btn2=Button(w,bg="#9d9d9d", fg="#0e0e0e", text="D12", command=D12func)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
    
##########################

d20lbl=Label(w,text=".", bg="#9d9d9d", fg="#ffffff")
d20lbl.place(relx=0.5, rely=0.6, anchor=CENTER)

def D20func():
    ACT2=random.choice(D20)
    d20lbl.config(text="You Rolled  "+ACT2)

btn3=Button(w,bg="#9d9d9d", fg="#0e0e0e", text="D20", command=D20func)
btn3.place(relx=0.5, rely=0.7, anchor=CENTER)
    

################################


w.mainloop()