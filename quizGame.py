from tkinter import *
root = Tk()
root.geometry("500x353")
root.title("Quiz Game")
root.resizable(0, 0)  

questions = [
    "What does HTML stand for?",
    "What does CSS stand for?",
    "What is the role of a 'constructor' in object-oriented programming?",
    "What is the process of finding errors and fixing them within a program?",
    "Which programming language is commonly used for creating Android applications?",
    "What is the most popular programming language for developing web applications?",
    "What does SQL stand for?",
    "What is the main difference between a tuple and a list in Python?",
    "What is the purpose of the 'git clone' command in Git?",
    "What does API stand for in programming?"
]

options = [
    ["Hyper Text Markup Language", "High Text Markup Language", "Hyper Tabular Markup Language", "High Tabular Markup Language"],
    ["Computer Style Sheets", "Cascading Style Sheets", "Creative Style Sheets", "Colorful Style Sheets"],
    ["It is used to initialize the object's state", "It is used to define a new class", "It is used to print output on the console", "It is used to import external libraries"],
    ["Debugging", "Compiling", "Running", "Editing"],
    ["Java", "Python", "Kotlin", "Swift"],
    ["Python", "JavaScript", "C++", "Ruby"],
    ["Structured Query Language", "Stylish Question Language", "Standard Query Language", "Stylish Query Language"],
    ["Lists are mutable, tuples are immutable", "Tuples are mutable, lists are immutable", "Both are mutable", "Both are immutable"],
    ["To create a copy of a Git repository", "To delete a Git repository", "To merge a Git repository", "To rename a Git repository"],
    ["Advanced Programming Interface","Application Programming Interface", "Application Python Interface", "Advanced Python Interface"]
]

answers = [1, 2, 1, 1, 3, 2, 1, 1, 1, 2]

score = 0
totalQuestions=10
questionNo=1

def start():
    welcomeScreen.pack_forget()
    f.pack(expand=True, fill=BOTH)

def next():
    global questionNo
    
    questionNo = questionNo+1
    if questionNo > totalQuestions:
        f.pack_forget()
        root.config(background="#9ce1ff")
        scoreScreen.pack()
        scoreScreen.config(background="#9ce1ff",text="SCORE: " + str(score),pady=100)
        playAgainButton.pack()
    else:
        option1.config(state=NORMAL)
        option2.config(state=NORMAL)
        option3.config(state=NORMAL)
        option4.config(state=NORMAL)
        val.set(0)
        feedback.pack_forget()
        question.config(text=questions[questionNo-1])
        option1.config(text=options[questionNo-1][0])
        option2.config(text=options[questionNo-1][1])
        option3.config(text=options[questionNo-1][2])
        option4.config(text=options[questionNo-1][3])
        if questionNo == totalQuestions:
            nextButton.config(text="CHECK SCORE")

def submit():
    global score
    if val.get()==0:
        selectedOption=0
    else:
        selectedOption = val.get()
        option1.config(state=DISABLED)
        option2.config(state=DISABLED)
        option3.config(state=DISABLED)
        option4.config(state=DISABLED)
    if (answers[questionNo-1] == selectedOption):
        feedback.pack()
        feedback.config(text="Correct Answer", foreground="green", font=("Segoe UI Bold", "15"))
        score=score+1
    elif (selectedOption==0):
        feedback.pack()
        feedback.config(text="Select Option",font=("Segoe UI Bold", "15"),foreground="black")
    else:
        feedback.pack()
        feedback.config(text="Wrong Answer",foreground="red",font=("Segoe UI Bold", "15"))

def playAgain():
    global score, questionNo
    score = 0
    questionNo = 1
    val.set(0)
    question.config(text=questions[questionNo-1])
    option1.config(text=options[questionNo-1][0])
    option2.config(text=options[questionNo-1][1])
    option3.config(text=options[questionNo-1][2])
    option4.config(text=options[questionNo-1][3])
    nextButton.config(text="NEXT QUESTION")
    playAgainButton.pack_forget()
    scoreScreen.pack_forget()
    f.pack(expand=True, fill=BOTH)
    option1.config(state="normal")
    option2.config(state="normal")
    option3.config(state="normal")
    option4.config(state="normal")
    feedback.pack_forget()



welcomeScreen = Frame(background="#9ce1ff")
welcomeScreen.pack()

introMessage=Label(welcomeScreen, text="QUIZ GAME",borderwidth=5,relief=SOLID, font=("Sitka Small Bold", 30), background="white", foreground="black", padx=500)
introMessage.pack(side=TOP)
instructions = Label(
    welcomeScreen,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Segoe UI Black",13),
    justify = "center",
    padx=150
)
instructions.pack()
rules = Label(welcomeScreen, text='1. There are a total of 10 questions in the quiz.\n2. Each question is worth 1 point.\n3. Select an answer and remember to submit it for it to count.\n4. After submitting your answer, click the "Next Question" button to proceed to the next question.', width = 100,font = ("Segoe UI Black",14),background = "#9ce1ff",foreground = "#063d0f", justify=LEFT, wraplength=500)
rules.pack(side=BOTTOM)
playButton = Button(welcomeScreen, text="START",command=start, font=("Courier New Bold", "20"),padx="10", borderwidth=5, relief=RAISED,background="white", foreground="black")
playButton.pack(pady="10")
f = Frame(background="#9ce1ff")
f.pack_forget()

question =Label(f, width=50, font=("Georgia Bold Italic", "15"), text = questions[0],background="#9ce1ff",wraplength=500)
question.pack(pady=10)

val = IntVar()
val.set(0)
option1=Radiobutton(f, text=options[0][0], variable=val, value=1, font=("Georgia Bold Italic", "13"),background="#9ce1ff")
option2=Radiobutton(f, text=options[0][1], variable=val, value= 2,font=("Georgia Bold Italic", "13"),background="#9ce1ff")
option3=Radiobutton(f, text=options[0][2], variable=val, value= 3,font=("Georgia Bold Italic", "13"),background="#9ce1ff")
option4=Radiobutton(f, text=options[0][3], variable=val, value=4,font=("Georgia Bold Italic", "13"),background="#9ce1ff")
feedback = Label(f, text="", background="#9ce1ff")
feedback.pack_forget()
option1.pack(side=TOP, anchor="w")
option2.pack(side=TOP, anchor="w")
option3.pack(side=TOP, anchor="w")
option4.pack(side=TOP, anchor="w")

submitButton=Button(f, text="SUBMIT ANSWER", command=submit, background="#06018f", foreground="white",font=("Courier New Bold", "15"))
submitButton.pack(pady="25")
nextButton = Button(f, text="NEXT QUESTION", command=next, background="#06018f", foreground="white",font=("Courier New Bold", "15"))
nextButton.pack(side=BOTTOM, anchor="e")

scoreScreen = Label(root,font=("Impact", "30"))
scoreScreen.pack_forget()

playAgainButton=Button(root, text="PLAY AGAIN", command=playAgain, background="red", foreground="white",font=("Courier New Bold", "15"))
playAgainButton.pack_forget()

root.mainloop() 