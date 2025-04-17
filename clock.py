from tkinter import Tk, Label
from time import strftime

def update():
    time_string= strftime("%H:%M")
    time_label.config(text=time_string)

    day_string= strftime("%A")
    day_label.config(text=day_string)

    date_string= strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window=Tk()

window.title("Clock")
window.geometry("800x400")
window.configure(background="black")

time_label=Label(window, font=("Casadica mono", 80, 'bold'), fg="green", bg="black")
time_label.pack()

day_label=Label(window, font=("Casadica mono", 30, 'bold'), bg="black", fg="green")
day_label.pack()

date_label=Label(window, font=("Casadica mono", 30, 'bold'), bg="black", fg="green")
date_label.pack()

update()

window.mainloop()