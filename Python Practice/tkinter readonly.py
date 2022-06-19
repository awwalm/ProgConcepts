from tkinter import *

window= Tk()
window.title('Read Only Entry Widget')
conOFentOutput= StringVar()
entOutput= Entry(window, width=20, state='readonly', textvariable=conOFentOutput)
entOutput.grid(padx=100, pady=15)
conOFentOutput.set('Hello World!')
window.mainloop()
