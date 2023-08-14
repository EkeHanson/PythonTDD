from tkinter import *

window = Tk()

photo = PhotoImage(file="logo.png")

label = Label(window, text="Abraham, E. Hanson", 
              font=("Arial", 40, 'bold'),
              fg="green",
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,BVV V
              image=photo)
              
              




label.pack()


window.config(background='#00ff00')




window.mainloop()