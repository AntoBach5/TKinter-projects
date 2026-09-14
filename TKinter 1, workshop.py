from tkinter import *
from datetime import date

window = Tk()
window.title("Workshop application")
window.geometry("600x450")

label1 = Label(text="Workshop Application", fg="black", bg="grey", height=1, width=400)
label2 = Label(text="Name + surname:", fg="black", bg="grey", height=1, width=400)

nameentry = Entry()

def display():
    name = nameentry.get()
    global message
    message = "You have signed up for the workshop! \nToday, "
    greet = "Hello " + name.capitalize() + "!"
    textbox1.insert(END, greet)
    textbox1.insert(END, message)
    textbox1.insert(END, date.today())
    
textbox1 = Text(height=3)
button1 = Button(text="Sign up", command=display, height=1, bg="grey", fg="black")

label1.pack()
label2.pack()
nameentry.pack()
textbox1.pack()
button1.pack()

window.mainloop()