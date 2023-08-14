from tkinter import *


root = Tk()
root.geometry('300x200')
f0 = Frame(root,width=300, height=50)
f0.pack()
logo = PhotoImage(file='logo.png')
lb1 = Label(f0,image=logo).pack()

f1 = Frame(root)
f1.pack()
label = Label(f1, text="Email")
label.grid(row=1,column=1)

wb1 = Entry(f1, bd = 5)
wb1.grid(row=1,column=2)
label2 = Label(f1,text="Password")
label2.grid(row=2,column=1) 
wb2 = Entry(f1,show='*',bd = 5)
wb2.grid(row=2,column=2)
label3 = Label(f1,text="Bug ID")
label3.grid(row=3,column=1)
wb3 = Entry(f1, bd = 5)
wb3.grid(row=3,column=2)

f2 = Frame(root) 
f2.pack()

def printdata():
     st = "Hello, Work in progress.."
     lab2 = Label(f2, text=st)
     lab2.grid(row=2, column=2)


but1 = Button(f2,text="Automate it", bg="blue", fg="white", 
command=printdata)
but1.grid(row=1,column=2)
root.mainloop()