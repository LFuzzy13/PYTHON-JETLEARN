from tkinter import *

#creating the window

Window=Tk()
Window.title("Favourite Dishes")
Window.geometry("300x500")
Window.config(bg="#811818")

#Making a List Box Object

#List=Listbox(Window, height=7, width=10, bg="#be9034")
#List.insert(1,"Spaghetti")
#List.insert(2,"Pizza")
#List.insert(3,"Lasagne")
#List.insert(4,"Bruschetta")
#List.insert(5,"Biriyani")
#List.place(relx=0.5, rely=0.5, anchor=CENTER)

#scrollbar

scrollbar=Scrollbar(Window)
scrollbar.pack(side=RIGHT, fill = Y)

#making a loop listbox

List2=Listbox(Window, bg="#48d86e", yscrollcommand=scrollbar.set, height=30, width=10, fg="#820f0f")
for i in range(120):
    List2.insert(END,"Mylo"+str(i))
List2.place(relx=0.2, rely=0.5, anchor=CENTER)
scrollbar.config(command=List2.yview)

#Creating Buttons
Btn=Button(Window,text="Exit.", bg="#780721", fg="#00ff22", font=("Comic Sans MS",20,"bold"),command=Window.destroy)
Btn.place(relx=0.7, rely=0.3, anchor=CENTER)

#creatign label
label1=Label(Window, text="How good is this list?", bg="#FFFFFF", fg="#ff00c8", font=("Times New Roman", 15, "italic"))
label1.place(relx=0.6, rely=0.6, anchor=CENTER)

input1=Entry(Window, fg="#ff00c8", font=("Comic Sans MS", 10, "italic"))
input1.place(relx=0.6, rely=0.7, anchor=CENTER)

Window.mainloop()