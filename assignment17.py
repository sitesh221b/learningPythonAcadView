from tkinter import *

#       QUESTION 1

x = Tk()
x.title("Assignments")
x.geometry('500x200')
label = Label(x, text='Hello World!', relief=FLAT, font=20)
bt = Button(x, text='Exit', width=5, command=x.destroy, activebackground='red', font=10)
label.pack()
bt.pack()


#       QUESTION 2

def func():
    lb = Label(x, text="I know you've clicked the button!", font=20)
    lb.pack()


bt1 = Button(x, text='Click Here!', font=20, width=20, command=func)
bt1.pack()


#       QUESTION 3

def label_function():
    lb.configure(text="Congratulations! You've been fooled!")


frame = Frame(x)
frame.pack()
topFrame = Frame(frame)
topFrame.pack(side=TOP)
leftFrame = Frame(frame)
leftFrame.pack(side=LEFT)
rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

bT = Button(leftFrame, text='ClickHere!', command=label_function, font=20, width=20)
bT.pack()
bT1 = Button(rightFrame, text='EXIT', font=20, width=20, command=x.destroy)
bT1.pack()
lb = Label(topFrame, text="Hey There!")
lb.pack()


#       QUESTION 4

def display():
    lB = Label(x, text=txt.get())
    lB.pack()


txt = Entry(x)
txt.pack()
txt.focus_set()

button = Button(x, text='Show', font=20, width=20, command=display)
button.pack()
x.mainloop()
