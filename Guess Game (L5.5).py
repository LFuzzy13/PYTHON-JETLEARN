from tkinter import *
import random
from tkinter import messagebox

W=Tk()
W.title("Guessinator 9000")
W.geometry("400x240")
W.config(bg="#7662a2")

#Functions v
def New_Game():
  global secret_number, attempts
  secret_number = random.randint(1, 100)
  attempts = 0
  Lbl2.config(text="I have picked a number between 1 and 100!")
  Entry1.delete(0,END)


def Guess_button():
  global attempts
  Guess=Entry1.get()

  if not Guess.isdigit():
           Lbl2.config(text="✖️ Please enter a valid number!")
           messagebox.showinfo("Invalid Number", "Please enter a valid number")
           return

  Guess = int(Guess)
  attempts +=1
  if Guess < secret_number:
      Lbl2.config(text=f"↓ Too Low! Attempts:{attempts}")
  elif Guess > secret_number:
      Lbl2.config(text=f"↑ Too High! Attempts: {attempts}")
  else:
      Lbl2.config(text=f"🎉 Correct! The number was {secret_number}. Attempts: {attempts}")
      messagebox.showinfo("Congratulations!", "Congrats! You Won!")

#Functions ^

#labels
Lbl1=Label(W,text="Guess The Number Between 1 - 100!!!", bg="#7662a2", fg="#DBA532", font=("impact", 15,"bold"))
Lbl1.pack()

Lbl2=Label(W,text=".", bg="#7662a2", fg="#D49828", font=("Arial", 10,"bold"))
Lbl2.pack()

Entry1=Entry(W,bg="#473465", fg="#cbbfe6")
Entry1.pack()

Btn1=Button(W,text="Guess", bg="#473465", fg="#b98927", font=("arial", 12, "bold"), command=Guess_button)
Btn1.place(relx=0.5, rely=0.4, anchor=CENTER)

Btn2=Button(W,text="Reset", bg="#473465", fg="#c68b32", font=("arial", 12, "bold"), command=New_Game)
Btn2.place(relx=0.5, rely=0.55, anchor=CENTER)

Btn=Button(W,text="Exit.", bg="#473465", fg="#c39529", font=("Arial",12,"bold"),command=W.destroy)
Btn.place(relx=0.5, rely=0.7, anchor=CENTER)


W.mainloop()