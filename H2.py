from tkinter import *

#title

W=Tk()
W.title("Please login!")
W.geometry("400x200")
W.config(bg = ("#c1c1c1"))

#functions

def VE(P):
    max_length=10
    if len (P) <= max_length:
        return True
    else:
        return False
    
Validatecomm = (W.register(VE),"%P")
    


#coding user name input
UN = Label(W, text = "Enter Username.", bg = "#c1c1c1", fg = "#1d1d1d")
UN.place(relx=0.2, rely=0.3, anchor=CENTER)
UNENTRY=Entry(W,bg="#8c8b8c",  fg="#2b2b2b", font=("Comic Sans MS", 10, "bold"), width="26")
UNENTRY.place(relx=0.6, rely=0.3, anchor=CENTER)

#password input
passw = Label(W, text = "Enter Password.", bg = "#c1c1c1", fg = "#1d1d1d")
passw.place(relx=0.2, rely=0.5, anchor=CENTER)
passin=Entry(W,bg="#8c8b8c",  fg="#292929", font=("Comic Sans MS", 10, "bold"), width="26", show="-", validate="key", validatecommand=Validatecomm)
passin.place(relx=0.6, rely=0.5, anchor=CENTER)

#buttons
Btn=Button(W,text="Cancel", bg="#BCBCBC", fg="#191919", font=("Comic Sans MS",10,"bold"),command=W.destroy)
Btn.place(relx=0.8, rely=0.7, anchor=CENTER)

Btn2=Button(W,text="log in", bg="#BCBCBC", fg="#191919", font=("Comic Sans MS",10,"bold"),command=W.destroy)
Btn2.place(relx=0.3, rely=0.7, anchor=CENTER)




W.mainloop()