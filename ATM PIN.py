from tkinter import *

window = Tk()
window.title("ATM PIN")
window.geometry("600x450")

frame = Frame(master=window, height=200, width=565, relief=SUNKEN, borderwidth=3, bg="lightblue")
frame.place(x=20, y=0)

label1 = Label(frame, text="Fullname", bg="green", fg="white", width=12)
label2 = Label(frame, text="Enter PIN", bg="green", fg="white", width=12)

name_entry = Entry(frame, width=12)
pin_entry = Entry(frame, width=12, show="*")

label1.place(x=20, y=20)
label2.place(x=20, y=80)
name_entry.place(x=150, y=20)
pin_entry.place(x=150, y=80)

nums = [
    [9, 8, 7], 
    [6, 5, 4],
    [3, 2, 1], 
    ["#", 0, "*"]
]

def signed_in():
    name = name_entry.get()
    pin = pin_entry.get()
    
    welcome = "Welcome "+name
    message = "\nYou have signed in succesfully! \n\nYour PIN is: "+pin
    
    textbox.insert(END, welcome)
    textbox.insert(END, message)
    textbox.place(x=100, y=250)
        

numpad_frame = Frame(master=window)
numpad_frame.place(x=350, y=20) 


def button_click(number):
    pin_entry.insert(END, number)


for i in range(4):
    for j in range(3):
        button_frame = Frame(
            master=numpad_frame, 
            relief=SUNKEN, 
            borderwidth=1
        )
        button_frame.grid(row=i, column=j, padx=2, pady=2)
 
        # (SEARCHED IN GOOGLE) The lambda n=... is a way in Tkinter to freeze the specific number into the button
        button = Button(master=button_frame, text=nums[i][j], bg="green", fg="white", width=4, height=2,
                     command=lambda n=nums[i][j]: button_click(n))
        button.pack(padx=3, pady=3, fill=BOTH, expand=True)
        

textbox = Text(bg="blue", fg="black", width=60, height=5)

button1 = Button(text="Create account", command=signed_in, bg="blue", fg="white")
button1.place(x=130, y=210)

window.mainloop()