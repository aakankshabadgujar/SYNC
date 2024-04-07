from tkinter import *
from datetime import datetime
from time import *
from pygame import mixer
from tkinter import messagebox


 

window = Tk()
window.title("Alarm Clock")
window.geometry("650x450")
alarmtime = StringVar()
msgi = StringVar()

head = Label(window, text="Alarm Clock",font=("comic sans", 30))
head.grid(row=0,column=3,pady = 35)

mixer.init()

def ala():
    a = alarmtime.get()
    Alarm = a
    CurrentTime = datetime.now().strftime("%H:%M")
    while Alarm != CurrentTime:
        CurrentTime = datetime.now().strftime("%H:%M")
        
    if Alarm == CurrentTime:
         mixer.music.load("alarmsound.wav")
         mixer.music.play()
         msgh = messagebox.showinfo("Info",f"{msgi.get()}")
         if msgh == "ok":
            mixer.music.stop()
            
            
        
    

Clockimg = PhotoImage(file="alarmclock.png")
new_image = Clockimg.zoom(1, 1)
new_image = new_image.subsample(6, 6)
img = Label(window, image=new_image)
img.grid(row=3,column=0)

input = Label(window, text="Input time",font=("Arial",18))
input.grid(row=2,column=3)

altime = Entry(window,textvar=alarmtime,font=("Arial",18),width = 6)
altime.grid(row=2,column=4)

msg = Label(window,text="Message",font=("Arial",18))
msg.grid(row=2,column=3,rowspan=4)

msginput = Entry(window,textvar=msgi,font=("Arial",25))
msginput.grid(row=4,column=3)

submit = Button(window,text="Submit",font=("Arial", 20),command = ala)
submit.grid(row=5, column=3)
window.mainloop()