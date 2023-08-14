from tkinter import *

count = 0

def click():
    global count
    
    count +=1
    print('You clicked me', count, 'times')


window = Tk()
window.title('Musixapp')

# label = Label(window, 
#               text='Hello World', 
#               font=('Arial', 30, 'bold'), 
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#             #   image=photo
#               )
# # label.place(x=100, y=100)
# label.pack()

button = Button(window, 
                text='Click Me',
                command=click,
                font=('Comic Sans', 30),
                fg='#00FF00',
                bg='black',
               activeforeground='#00FF00',
               activebackground='black',
               state=ACTIVE,
            #    image=photo,
            # compound='bottom' #This set the image position relative to the button text
               )
button.pack()

window.mainloop()