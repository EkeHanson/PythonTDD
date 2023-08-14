from tkinter import *

count = 0

def submit():
    username = entry.get()
    print('Hello', username)
    print(len(entry.get()))
    entry.config(state=DISABLED)

def delete():
    username = entry.delete(0, END) 
def backspace():
    entry.delete(len(entry.get()) -1, END)
window = Tk()
window.title('Musixapp')
entry = Entry(window,
            font=('Comic Sans', 50),
            fg='#00FF00',
            bg='black')
entry.insert(0, 'enter your requests')
entry.pack(side=TOP)
submit_button = Button(window,
                       text='Submit',
                        command=submit)
submit_button.pack(side=BOTTOM)

delete_button = Button(window,
                       text='Delete',
                        command=delete)
delete_button.pack(side=RIGHT)
backspace_button = Button(window,
                       text='Clear',
                        command=backspace)
backspace_button.pack(side=RIGHT)
window.mainloop()