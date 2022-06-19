from tkinter import *

def changeColor():
    if btnCalculate['fg'] == 'blue':
        btnCalculate['fg'] = 'red'
    else:
        btnCalculate['fg'] = 'blue'

def convertToUpperCase(event):
    conOFentName.set(conOFentName.get().upper())

window= Tk()
window.title('Button')

btnCalculate= Button(window, text='Calculate',bg= 'grey', fg= 'blue', command=changeColor)
btnCalculate.grid(padx=150, pady=100)

lblPrincipal= Label(window, bg='orange', fg='green', text= 'Principal: ')
lblPrincipal.grid(padx=1, pady=1)

conOFentName= StringVar()
entName= Entry(window, fg='blue', textvariable=conOFentName)
entName.grid(padx=1, pady=1)
entName.bind('<Button-3>', convertToUpperCase)
window.mainloop()
