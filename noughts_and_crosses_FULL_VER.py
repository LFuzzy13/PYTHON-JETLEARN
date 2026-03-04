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
    
    edge = []
    for i in possiblemove:
        if i in [[0,1], [1,0], [1,2], [2,1]]:
            edge.append(i)

    if len(edge) > 0 :
           move = random.randint(0,len(edge) - 1)
           return edge[move]
    
def get_text_pc(i,j,gb,l1,l2):
    global Sign

    if board[i][j] == " ":
        if Sign%2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            btn1[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"

        Sign +=1
        btn1[i][j].config(text=board[i][j])

    x = True

    if winner(board,"X"):
        gb.destroy()
        x=False
        box=messagebox.showinfo("Winner","Player Won The Match")

    elif winner(board, "O"):
         gb.destroy()
         x=False
         box=messagebox.showinfo("Winner","Computer Won The Match")

    elif isfull():
        gb.destroy()
        x=False
        box=messagebox.showinfo("Tie Game", "The Game Was A Tie")
    
    if x:
        if Sign % 2 !=0:
            move = PC()
            btn1[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0],move[1],gb,l1,l2)

def gameboard_pc(game_board,l1,l2):
    global btn1
    btn1=[]

    for i in range(3):
        m = 3+i 
        btn1.append(i)
        btn1[i] = []
        for j in range(3):
            n= j
            btn1[i].append(j)
            get_t = partial(get_text_pc,i,j,game_board,l1,l2)
            btn1[i][j]=Button(game_board,bd=5,command=get_t,height=4,width=8)
            btn1[i][j].grid(row=m,column=n)
    game_board.mainloop()

def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Noughts & Crosses")
    
    l1=Button(game_board,text = "Player : X", width=10)
    l1.grid(row = 1,column = 1)

    l2=Button(game_board,text = "Player : O", width=10, state=DISABLED)
    l2.grid(row = 2,column = 1)

    gameboard_pc(game_board,l1,l2)

def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Noughts & Crosses")
      
    l1=Button(game_board,text = "Player 1 : X", width=10)
    l1.grid(row = 1,column = 1)

    l2=Button(game_board,text = "Player 2 : O", width=10, state=DISABLED)
    l2.grid(row = 2,column = 1)

    gameboard_pl(game_board,l1,l2)

def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Noughts & Crosses")

    wpc=partial(withpc,menu)
    wpl=partial(withplayer,menu)
    head = Button(
        menu,
        text="-----Welcome to Noughts & Crosses-----",
        activeforeground='red',
        activebackground="yellow",
        bg="red",
        fg="yellow",
        width=500,
        font="summer",
        bd = 5
    )
    
    b1=Button(
        menu,text="Singleplayer",command=wpc,
        activeforeground="red", activebackground="yellow",
        bg="red",fg="yellow", width=500,
        font="summer", bd=5
    )

    b2=Button(
        menu,text="Multiplayer",command=wpl,
        activeforeground="red", activebackground="yellow",
        bg="red",fg="yellow", width=500,
        font="summer", bd=5
    )

    b3=Button(
        menu,text="Exit",command=menu.quit,
        activeforeground="red", activebackground="yellow",
        bg="red",fg="yellow", width=500,
        font="summer", bd=5
    )

    head.pack(side="top")
    b1.pack(side="top")
    b2.pack(side="top")
    b3.pack(side="top")

    menu.mainloop()

if __name__ == "__main__":
    play()