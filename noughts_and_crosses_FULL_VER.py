#import
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

#Variables
Sign = 0
global board

board = [[" " for x in range(3)] for y in range(3)]

#functions
def winner(b,l):
    return (
        #row checks        
        (b[0][0]==l and b[0][1]==l and b[0][2]==l) or
        (b[1][0]==l and b[1][1]==l and b[1][2]==l) or
        (b[2][0]==l and b[2][1]==l and b[2][2]==l) or
        #column checks
        (b[0][0]==l and b[1][0]==l and b[2][0]==l) or
        (b[0][1]==l and b[1][1]==l and b[2][1]==l) or
        (b[0][2]==l and b[1][2]==l and b[2][2]==l) or
        #Diagonal
        (b[0][0]==l and b[1][1]==l and b[2][2]==l) or
        (b[0][2]==l and b[1][1]==l and b[2][0]==l)

    )
    
def get_text(i,j,gb,l1,l2):
    global Sign
    if board [i][j]==" ":
        if Sign %2==0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j]="X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j]="O"
        Sign+=1
        btn1[i][j].config(text=board[i][j])
    
    if winner(board,"X"):
        gb.destroy()
        textbox = messagebox.showinfo("Winner!","Player 1 Won the Match")
    elif winner(board,"O"):
        gb.destroy()
        textbox = messagebox.showinfo("Winner!", "Player 2 Won the Match")
    elif isfull():
        gb.destroy()
        textbox = messagebox.showinfo("Tie", "The Game Was a Tie.")
        
def isfree(i,j):
    return board[i][j]==" "

def isfull():
    flag=True
    for i in board:
        if i.count(" ")>0:
            flag=False
    return flag

def gameboard_pl(gameboard,l1,l2):
    global btn1
    btn1 = []
    for i in range(3):
        m=3+i
        btn1.append(i)
        btn1[i]=[]
        for j in range(3):
            n=j
            btn1[i].append(j)    
            get_t=partial(get_text,i,j,gameboard,l1,l2)
            btn1[i][j]=Button(gameboard,bd=5, command=get_t, height = 4, width = 8)
            btn1[i][j].grid(row=m,column=n)
    gameboard.mainloop()

def PC():
    possiblemove=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                possiblemove.append([i,j])
    move=[]    
    if possiblemove==[]:
        return
    else:
        for let in ["O","X"]:
            for i in possiblemove:
                boardcopy=deepcopy(board)
                boardcopy[i[0]][i[1]]=let
                if winner(boardcopy,let):
                    return i
    corner = []
    for i in possiblemove:
        if i in [[0,0],[0,2],[2,0],[2,2]]:
            corner.append(i)
    if len (corner)>0:
        move = random.randint(0,len(corner)-1) 
        return corner[move]
    #INCOMPLETE
