from tkinter import *

window= Tk()
window.title('ReadOnly Entry Widget')
conOFentOutput= StringVar()
entOutput = Entry(window, state='readonly', textvariable=conOFentOutput)
entOutput.grid(padx=100, pady=15)
conOFentOutput.set('Hello World!')
window.mainloop()
