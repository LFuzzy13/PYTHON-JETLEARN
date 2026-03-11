from tkinter import *
from tkinter import messagebox

W=Tk()
W.title("Tic Tac Toe DEMO")

Turn = 1
Result = ""

def WinFunc():
    global Result
    if B1.cget("text")==B2.cget("text")==B3.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B1.cget("text")==B2.cget("text")==B3.cget("text")=='O':
        Result = "Player 2 Wins"

    elif B4.cget("text")==B5.cget("text")==B6.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B4.cget("text")==B5.cget("text")==B6.cget("text")=='O':
        Result = "Player 2 Wins"
    
    elif B7.cget("text")==B8.cget("text")==B9.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B7.cget("text")==B8.cget("text")==B9.cget("text")=='O':
        Result = "Player 2 Wins"
#collumns
    elif B1.cget("text")==B4.cget("text")==B7.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B1.cget("text")==B4.cget("text")==B7.cget("text")=='O':
        Result = "Player 2 Wins"

    elif B2.cget("text")==B5.cget("text")==B8.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B2.cget("text")==B5.cget("text")==B8.cget("text")=='O':
        Result = "Player 2 Wins"
    
    elif B3.cget("text")==B6.cget("text")==B9.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B3.cget("text")==B6.cget("text")==B9.cget("text")=='O':
        Result = "Player 2 Wins"
 
#Diagonals
    
    elif B1.cget("text")==B5.cget("text")==B9.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B1.cget("text")==B5.cget("text")==B9.cget("text")=='O':
        Result = "Player 2 Wins"

    elif B3.cget("text")==B5.cget("text")==B7.cget("text")=='X':
        Result = "Player 1 Wins"

    elif B3.cget("text")==B5.cget("text")==B7.cget("text")=='O':
        Result = "Player 2 Wins"
    
    else:
        return
    

    messagebox.showinfo("Result", str(Result))
    W.destroy()

def B1click():
    global Turn
    mytext=B1.cget('text')
    if mytext == '':
        if Turn == 1:
            B1.configure(text="X")
            Turn = 2
        else:
            B1.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B2click():
    global Turn
    mytext=B2.cget('text')
    if mytext == '':
        if Turn == 1:
            B2.configure(text="X")
            Turn = 2
        else:
            B2.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B3click():
    global Turn
    mytext=B3.cget('text')
    if mytext == '':
        if Turn == 1:
            B3.configure(text="X")
            Turn = 2
        else:
            B3.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B4click():
    global Turn
    mytext=B4.cget('text')
    if mytext == '':
        if Turn == 1:
            B4.configure(text="X")
            Turn = 2
        else:
            B4.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B5click():
    global Turn
    mytext=B5.cget('text')
    if mytext == '':
        if Turn == 1:
            B5.configure(text="X")
            Turn = 2
        else:
            B5.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B6click():
    global Turn
    mytext=B6.cget('text')
    if mytext == '':
        if Turn == 1:
            B6.configure(text="X")
            Turn = 2
        else:
            B6.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B7click():
    global Turn
    mytext=B7.cget('text')
    if mytext == '':
        if Turn == 1:
            B7.configure(text="X")
            Turn = 2
        else:
            B7.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B8click():
    global Turn
    mytext=B8.cget('text')
    if mytext == '':
        if Turn == 1:
            B8.configure(text="X")
            Turn = 2
        else:
            B8.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

def B9click():
    global Turn
    mytext=B9.cget('text')
    if mytext == '':
        if Turn == 1:
            B9.configure(text="X")
            Turn = 2
        else:
            B9.configure(text="O")
            Turn=1
        label.configure(text="Player"+str(Turn)+"Turn")
        WinFunc()

#BUTTONS

B1=Button(W,text="",width=5,command=B1click, bg="#6c2989")
B1.grid(row=0, column=0,padx=5, pady=5)

B2=Button(W,text="",width=5,command=B2click, bg="#6c2989")
B2.grid(row=0, column=1,padx=5, pady=5)

B3=Button(W,text="",width=5,command=B3click, bg="#6c2989")
B3.grid(row=0, column=2,padx=5, pady=5)

B4=Button(W,text="",width=5,command=B4click, bg="#6c2989")
B4.grid(row=1, column=0,padx=5, pady=5)

B5=Button(W,text="",width=5,command=B5click, bg="#6c2989")
B5.grid(row=1, column=1,padx=5, pady=5)

B6=Button(W,text="",width=5,command=B6click, bg="#6c2989")
B6.grid(row=1, column=2,padx=5, pady=5)

B7=Button(W,text="",width=5,command=B7click, bg="#6c2989")
B7.grid(row=2, column=0,padx=5, pady=5)

B8=Button(W,text="",width=5,command=B8click, bg="#6c2989")
B8.grid(row=2, column=1,padx=5, pady=5)

B9=Button(W,text="",width=5,command=B9click, bg="#6c2989")
B9.grid(row=2, column=2,padx=5, pady=5)

label=Label(W,text="Player" +str(Turn) +"Turn", bg="#dfb65d")
label.grid(row=3,column=1,padx=10,pady=10)

W.mainloop()