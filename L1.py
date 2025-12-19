from tkinter import *
#Creating The Window
Window = Tk()
Window.title("Dont Click The Button!")
Window.geometry("500x500")
Window.config(bg="#63baa7")
#Creating Buttons
Btn=Button(Window,text="Dont Click Me.", bg="#cf0c3a", fg="white", font=("Arial",20,"bold"),command=Window.destroy)
Btn.place(relx=0.5, rely=0.5, anchor=CENTER)
#progress
#P=progressbar(master, option=value)

Window.mainloop()