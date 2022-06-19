from tkinter import *

window= Tk()
window.title('Scrollbar')
xscroll= Scrollbar(window, width=20, orient=HORIZONTAL)
xscroll.grid(padx=150, pady=20)
window.mainloop()
#
