from tkinter import *
from gtts import gTTS
from googletrans import Translator
import os

window=Tk()
entry=Entry(window,width=40,font=14)
entry.pack(pady=20)
translator=Translator()

def play():
    text=entry.get()
    translated=translator.translate(text,dest="fr")
    french_text=translated.text
    speech=gTTS(text=french_text,lang="fr")
    speech.save("french.mp3")
    os.system("french.mp3")

btn=Button(window,text="Speak in french",command=play)
btn.pack(pady=20)
window.mainloop()
