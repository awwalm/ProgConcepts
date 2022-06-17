from tkinter import *

window= Tk()
window.title('Scrollbar')
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(padx=110, pady=15)
window.mainloop()
