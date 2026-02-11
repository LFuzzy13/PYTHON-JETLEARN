import time 
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("350x250")
root.title("Exam Timer Test")
root.config(bg="#7e7e7e")

running=False

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

Label(root, text="hour", bg="#7e7e7e").place(x=85, y=0)
Label(root, text="minutes", bg="#7e7e7e").place(x=135, y=0)
Label(root, text="seconds", bg="#7e7e7e").place(x=190, y=0)

hourEntry=Entry(root, width = 3, font=("Arial", 18), textvariable=hour, bg="#7e7e7e")
hourEntry.place(x=80, y=25)

minuteEntry=Entry(root, width = 3, font=("Arial", 18), textvariable=minute, bg="#7e7e7e")
minuteEntry.place(x=130, y=25)

secondsEntry=Entry(root, width = 3, font=("Arial", 18), textvariable=second, bg="#7e7e7e")
secondsEntry.place(x=180, y=25)

def start_timer():
    global running
    running = True

    try:
        temp = int(hour.get()) * 3600 + int (minute.get()) * 60 + int(second.get())
    except:
        messagebox.showerror("error","Please enter valid number")
        return
    
    while temp >=0 and running:
        mins, secs = divmod(temp, 60)
        hrs = 0

        if mins >=60:
            hrs, mins = divmod(mins, 60)
        
        hour.set("{0:02d}".format(hrs))
        minute.set("{0:02d}".format(mins))
        second.set("{0:02d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Time Countdown","Times up!!!")
            running= False

        if temp <= 10:
            secondsEntry.config(fg="#c42b2b")

        temp -=1
def stop_timer():
    global running
    running = False

startBtn = Button(root, text="Start Exam", width =10, bd=5, command=start_timer, bg="#7e7e7e")
startBtn.place(x=70, y=120)

stopBtn = Button(root, text="Stop Exam", width =10, bd=5, command=stop_timer, bg="#7e7e7e")
stopBtn.place(x=190, y=120)

root.mainloop()



