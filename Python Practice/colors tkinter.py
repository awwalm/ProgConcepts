from tkinter import *

def chooseColor(event):
    lstColors['bg']=lstColors.get(lstColors.curselection())

window= Tk()
window.title('Colors')
L= 'red', 'yellow', 'light blue', 'orange', 'black'
conOFcolors= StringVar()
lstColors= Listbox(window, width=8, height=5, listvariable=conOFcolors)
lstColors.grid(padx=100, pady=15)
conOFcolors.set(L)
lstColors.bind('<<ListboxSelect>>', chooseColor)
window.mainloop()
