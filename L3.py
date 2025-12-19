from tkinter import *

w=Tk()
w.title("OH MA GAWWWWSH")
w.geometry("400x200")
w.config(bg="#ff9f9f")

in1=Entry(w, bg="#d86c6c", fg="#3F1F1F")
in1.pack()

lbl=Label(w, bg="#d86c6c", fg="#3F1F1F")
lbl.pack()

def INFO1():
    getinfo=in1.get()
    lbl.config(text=getinfo)


btn1=Button(w,bg="#d86c6c", fg="#3F1F1F", text="Hi", command=INFO1)
btn1.pack()

Btn=Button(w,text="Close Window", bg="#d86c6c", fg="#3F1F1F", command=w.destroy)
Btn.pack()


w.mainloop()