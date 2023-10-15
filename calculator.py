from tkinter import *
root = Tk()
root.geometry("442x416") 
root.resizable(0, 0)  
root.title("Calculator")

def click(event):
    global screenVar
    text = event.widget.cget("text")
    if text == "=":
        if screenVar.get().isdigit():
            value = int(screenVar.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        screenVar.set(value)
        screen.update()
    elif text == "C":
        screenVar.set("")
        screen.update()
    else:
        screenVar.set(screenVar.get() + text)
        screen.update()
 
    
screenVar = StringVar() 
screenVar.set("")
screen = Entry(root, font='arial 18 bold', textvariable=screenVar, width=50, borderwidth=5, relief=SUNKEN)
screen.grid(row=0, column=0)
screen.pack(ipady=10)

f = Frame(root, width=312, height=272.5, bg="grey")
f.pack()

clearButton=Button(f,text="C",width="32",font=("arial bold", 12), height="3", cursor = "hand2",fg="white", bg="black")
clearButton.pack(side=LEFT)
clearButton.bind('<Button-1>',click)

divideButton = Button(f, text = "/",font=("arial bold", 12), width = 10, height = 3, cursor = "hand2",fg="white", bg="black")
divideButton.pack(side=LEFT)
divideButton.bind('<Button-1>',click)

buttons = ['7', '8', '9', '*']
f = Frame(root, width=312, height=272.5, bg="grey")
f.pack()
for b in buttons:
    buttonsInRow2 = Button(f, text = b ,font=("arial bold", 12), width = 10, height = 3, cursor = "hand2",fg="white", bg="black")
    buttonsInRow2.pack(side=LEFT)
    buttonsInRow2.bind('<Button-1>', click)

buttons = ['4', '5', '6', '-']
f = Frame(root, width=312, height=272.5, bg="grey")
f.pack()
for b in buttons:
    buttonsInRow3 = Button(f, text = b ,font=("arial bold", 12), width = 10, height = 3, cursor = "hand2",fg="white", bg="black")
    buttonsInRow3.pack(side=LEFT)
    buttonsInRow3.bind('<Button-1>', click)

buttons = ['1', '2', '3', '+']
f = Frame(root, width=312, height=272.5, bg="grey")
f.pack()
for b in buttons:
    buttonsInRow4 = Button(f, text = b,font=("arial bold", 12),width = 10, height = 3, cursor = "hand2",fg="white", bg="black")
    buttonsInRow4.pack(side=LEFT)
    buttonsInRow4.bind('<Button-1>', click)

f = Frame(root, width=312, height=272.5, bg="grey")
f.pack()
zeroButton=Button(f, text='0',font=("arial bold", 12), width='21', height='3',cursor = "hand2",fg="white", bg="black")
zeroButton.pack(side=LEFT)
zeroButton.bind('<Button-1>', click)

pointButton=Button(f, text='=',font=("arial bold", 12), width='10', height='3',cursor = "hand2",fg="white", bg="black")
pointButton.pack(side=LEFT)
pointButton.bind('<Button-1>', click)

equalButton=Button(f, text='.',font=("arial bold", 12), width='10', height='3',cursor = "hand2",fg="white", bg="black")
equalButton.pack(side=LEFT)
equalButton.bind('<Button-1>', click)
root.mainloop()