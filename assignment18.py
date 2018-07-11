from tkinter import *

#       QUESTION 1

root = Tk()
values = values = {'Steve': '6781367092', 'Tony': '6536123852', 'Bruce': '7159346289', 'Peter': '7163246952'}
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
myList = Listbox(root, yscrollcommand=scroll.set)

for keys in values:
    myList.insert(END, keys)

myList.pack()


#       QUESTION 2

def add_items():
    values.update({name.get(): num.get()})
    myList.insert(END, name.get())


lb = Label(root, text="Enter Name: ")
lb.pack()
name = Entry()
name.pack()
lb1 = Label(root, text="Enter Phone: ")
lb1.pack()
num = Entry()
num.pack()
btn = Button(root, text="ADD", font=20, command=add_items)
btn.pack()
root.mainloop()
