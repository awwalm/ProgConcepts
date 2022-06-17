from tkinter import *

window = Tk()

window.title('Programming Concept - Mr Riyaz')

entName = Entry(window, width= 25)
entName.grid(padx=200, pady=60)

lblPrincipal = Label(window, text='IUMW: ')
lblPrincipal.grid(padx=100, pady=15)
window.mainloop()
