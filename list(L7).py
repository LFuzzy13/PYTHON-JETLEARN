from tkinter import *
from tkinter.filedialog import *

W=Tk()
W.title("list")

def openfilesource():
    fin=askopenfile(title='openfile')
    if fin is not None:
        listbox.delete(0,END)
        items=fin.readlines()
        for item in items:
            listbox.insert(END,item.strip())

def savingfile():
    fout=asksaveasfile(defaultextension='.txt')
    if fout is not None:
        for item in listbox.get(0,END):
            print(item.strip(),file=fout)

def additem():
    listbox.insert(END,item.get())
    item.delete(0,END)

def deleteitem():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

fopen=Button(W, text="open",command=openfilesource, width=15)
fdelete=Button(W, text="delete", command=deleteitem, width = 15)
fsave=Button(W,text="save", command=savingfile, width = 15)

fopen.pack(side=LEFT,padx=5,pady=5)
fdelete.pack(side=RIGHT,padx=5,pady=5)
fsave.pack(padx=5,pady=5)

BtnADD = Button (W, text="add", command=additem, width = 50)
item=Entry(W,width=35)
item.pack(padx=5,pady=5)
BtnADD.pack(padx=5,pady=5)

frame1 = Frame(W)
scrollbar=Scrollbar(frame1, orient="vertical")
scrollbar.pack(Side = RIGHT,fill = Y)
listbox = Listbox(frame1,width=70,yscrollcommand=scrollbar.set,bg="Red")

for i in range(1,100):
    listbox.insert(END,"LIST"+str(i))

listbox.pack(side = LEFT,padx=5)
scrollbar.config(command=listbox.yview)
frame1.pack(side = RIGHT)
W.mainloop()
