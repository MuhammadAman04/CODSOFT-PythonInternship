import random
import string
from tkinter import *
import pyperclip

 
root = Tk()

def password():
    global choice
    if choice.get()==1:
        return "".join(random.sample(weak, val.get()))
    elif choice.get()==2:
        return "".join(random.sample(medium, val.get()))
    elif choice.get()==3:
        return "".join(random.sample(strong, val.get()))
         

def generatePassword():
    global result
    result.delete(0, END)  
    result.insert(0,password())
    result.insert(0,password())

def copy():
    pyperclip.copy(result.get())

weak = string.ascii_uppercase + string.ascii_lowercase
medium = string.ascii_uppercase + string.ascii_lowercase  + string.digits
strong = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

root.geometry("308x332")
root.config(background="#63e4f2")

Label(root,text="PASSWORD GENERATOR", font=("Segoe UI Black Italic", "18"),borderwidth=3,relief=SOLID,padx=10,background="#e6e6e6").pack()
Label(root,background="#63e4f2").pack()
Label(root,text="SELECT LENGTH & STRENGTH", font=("Segoe UI Black Italic", "13"),padx=50,background="black", foreground="white").pack()
choice = IntVar()
b1 = Radiobutton(root,text="Weak", variable=choice, value=1, font=("Segoe UI Black", "10"), background="#63e4f2", foreground="black", )
b1.pack()
b2 = Radiobutton(root,text="Medium", variable=choice, value=2, font=("Segoe UI Black", "10"), background="#63e4f2", foreground="black", )
b2.pack()
b3 = Radiobutton(root,text="Strong", variable=choice, value=3, font=("Segoe UI Black", "10"), background="#63e4f2", foreground="black", )
b3.pack()

val = IntVar()
Spinbox(root,font=("Impact","20"), from_=0, to_=15, textvariable=val, width=2, justify=CENTER).pack(pady=10)
Button(root, text="GENERATE PASSWORD",font=("Segoe UI Black","10"),borderwidth=3,relief=RAISED, command=generatePassword).pack()

result= Entry(root,width=200, font=("Impact", "15"), background="#63e4f2",justify=CENTER)
result.pack(pady=5)

Button(root, text="COPY",font=("Segoe UI Black","10"),borderwidth=3,relief=RAISED, command=copy).pack(side=BOTTOM)
root.mainloop()
