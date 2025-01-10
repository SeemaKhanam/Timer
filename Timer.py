from tkinter import *
from playsound import playsound 
import time 

root=Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)

heading=Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)
#clock
Label(root,font=("arial",15,"bold"),text="current time:",bg="papaya whip").place(x=65,y=70)
def clock():
    clock_time=time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)
current_time=Label(root,font=("arial",15,"bold"),text="",fg="#000",bg="#fff")
current_time.place(x=190,y=70)
clock()

#timer 
hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="aerial 50",bg="#000",fg="#fff",bd=0).place(x=30,y=155)
hrs.set("00")

mins=StringVar()
Entry(root,textvariable=mins,width=2,font="aerial 50",bg="#000",fg="#fff",bd=0).place(x=150,y=155)
mins.set("00")

sec=StringVar()
Entry(root,textvariable=sec,width=2,font="aerial 50",bg="#000",fg="#fff",bd=0).place(x=270,y=155)
sec.set("00")

Label(root,text="hours",font="aerial 12",bg="#000",fg="#fff").place(x=105,y=200)
Label(root,text="mins",font="aerial 12",bg="#000",fg="#fff").place(x=225,y=200)
Label(root,text="sec",font="aerial 12",bg="#000",fg="#fff").place(x=345,y=200)



def Timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    
    def countdown():
        nonlocal times
        if times > 0:
            times -= 1
            minute, second = divmod(times, 60)
            hour, minute = divmod(minute, 60)
            hrs.set(f"{hour:02}")
            mins.set(f"{minute:02}")
            sec.set(f"{second:02}")
            root.after(1000, countdown)  # Call countdown again after 1 second
        else:
            playsound(r"C:\Users\Seema\Downloads\buzzer-17-203422.mp3")
            sec.set("00")
            mins.set("00")
            hrs.set("00")

    countdown()  # Start the countdown
running=False
  
def restart():
    global running
    running = False  # Stop the timer
    hrs.set("00")
    mins.set("00")
    sec.set("00")      
def brush():
    hrs.set("00")
    mins.set("02")
    sec.min("00")

def eggs():
    hrs.set("00")
    mins.set("10")
    sec.min("00")

def face():
    hrs.set("00")
    mins.set("15")
    sec.min("00")
    
button=Button(root,text="Start",bg="#ea3548",bd=0,fg="#fff",width=20,height=2,font="arial 10 bold",command=Timer)
button.pack(padx=5,pady=10,side=BOTTOM)

restart_button = Button(root, text="Restart", bg="#4CAF50", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=restart)
restart_button.pack(padx=5, pady=10, side=BOTTOM)
Image1=PhotoImage(file=r"C:\Users\Seema\Downloads\eggs.png")
button1=Button(root,image=Image1,bg="#000",bd=0,command=eggs)
button1.place(x=7,y=300)

Image2=PhotoImage(file=r"C:\Users\Seema\Downloads\brush.png")
button2=Button(root,image=Image2,bg="#000",bd=0,command=brush)
button2.place(x=137,y=300)

Image3=PhotoImage(file=r"C:\Users\Seema\Downloads\face.png")
button3=Button(root,image=Image3,bg="#000",bd=0,command=face)
button3.place(x=267,y=300)
root.mainloop()