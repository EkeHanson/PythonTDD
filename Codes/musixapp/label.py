from tkinter import *
window = Tk()
window.title('Musixapp')

# photo = PhotoImage(file='logo.png')

label = Label(window, 
              text='Hello World', 
              font=('Arial', 40, 'bold'), 
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
            #   image=photo
              )
# label.place(x=100, y=100)
label.pack()



window.mainloop()

