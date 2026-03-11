from tkinter import *
from gtts import gTTS
import os 

window = Tk()
frame1=Frame(window,bg="#7effce", height="150")
frame1.pack(fill=X)

frame2=Frame(window,bg="#373737", height = "750")
frame2.pack(fill=X)

label=Label(frame1,text="Text-To-Speech",font="bold,30",bg="#8F8F8F")
label.place(x=265,y=70)

entry1=Entry(frame2,width=45,bd=4,font="14")
entry1.place(x=70,y=52)
entry1.insert(0,"")

def play():
    language="lv"
    myobj=gTTS(text=entry1.get(),lang=language,slow=False,tld="fr")
    myobj.save("convert.wav")
    os.system("convert.wav")

btn=Button(frame2,text="Submit",width=15,pady=10,font="bold,15",command=play,bg="#bebdbd")
btn.place(x=250,y=130)

window.title("Text to speech converter")
window.geometry("650x550+350+200")
window.mainloop()