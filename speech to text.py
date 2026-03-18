from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

window=Tk()
window.title("SPEECH TO TEXT")
window.geometry("1000x400")
heading1=Label(window,text="voice notepad",font=("arial",30,"bold"))
heading1.grid(row=0,column=1,padx=20,pady=20)
output_text=Text(window,height=6,width=40,font=("arial",12))
output_text.grid(row=1,column=1,pady=20,padx=20)

def Translate():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("speak anything.")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            text="sorry, couldn't recognize your voice, please try again."
    output_text.delete(1.0,END)
    output_text.insert(END,text)

def save():
    fout=asksaveasfile(defaultextension=".txt")
    if fout:
        fout.write(output_text.get(1.0,END))
        fout.close()
        messagebox.showinfo("Saved file.","File saved successfully")
    else:
        messagebox.showinfo("WARNING!","TEXT NOT SAVED!")

T_Btn=Button(
    window,
    text="Start Recording",
    command=Translate,
    font=("Arial",15,"bold"),
    width=20,
    bg="#4CAF50",
    fg="white"
)

T_Btn.grid(row=1,column=0,pady=20,padx=20)

Save_button=Button(
    window,
    text="Save The Text",
    font=("Arial",12,"bold"),
    width=20,
    height=4,
    command=save,
    bg="#2196F3",
    fg="white"
)
Save_button.grid(row=1,column=2,pady=10)

window.mainloop()