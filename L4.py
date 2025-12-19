from tkinter import *
W=Tk()
W.geometry("300x200")
W.config(bg="#2D2D3B")
W.resizable(False,False)
W.title("Temperature Calculator")

#Conversion Function
def fun1():
    try:
        temp = float(Entry1.get())
        if var.get() == 1: #celsius to fahrenheit
            Fah = (temp *1.8 ) + 32
            lblOUTPUT.config(text=str(Fah)+"°F")
        else: # fahrenheit to celsius
            Cel = (temp -32) /1.8
            lblOUTPUT.config(text=str(Cel)+"°C")
    except ValueError:
        lblOUTPUT.config(text="Please A Valid Number")



        

lbl1=Label(W, bg="#2D2D3B",fg="#c9c9de",text="Temperature Calculator",font=("Arial",13))
lbl1.pack()

lbl2=Label(W, bg="#2D2D3B",fg="#c9c9de",text="Enter Temperature:",font=("Arial",7))
lbl2.pack()

Entry1=Entry(W,bg="#3b3b49", fg="#c9c9de")
Entry1.pack()

var=IntVar(value=1)
Radiobutton(W,text="Celsius ⇒ Fahrenheit",variable=var,value=1, bg="#2D2D3B", fg="#5858c9").pack()
Radiobutton(W,text="Fahrenheit ⇒ Celsius", variable=var, value=2, bg="#2D2D3B", fg="#5858be").pack()

btn1=Button(bg="#3b3b49", fg="#c9c9de", text="Convert", command=fun1)
btn1.pack()

lblOUTPUT=Label(W, bg="#2D2D3B", fg="#11C923",text="PLACEHOLDER TEXT", font=("Times New Roman",10,"bold"))
lblOUTPUT.place(rely=0.75, relx=0.5, anchor=CENTER)

Btn=Button(W,text="Close", bg="#2D2D3B", fg="#c9c9de", command=W.destroy)
Btn.place(rely=0.9, relx=0.5, anchor=CENTER)


W.mainloop()