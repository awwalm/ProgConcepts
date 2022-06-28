from tkinter import *

def showInfo(event):
    i = listbox.curselection()
    index = int(i[0])
    cont.set(contient[index])
    pop.set(population[index])
    area.set(areaKm2[index])

window = Tk()
window.title("Members of U.N.")
countries = ["Eritrea", "Estonia","Ethiopia","Fiji","Finland",
             "France","Gabon","Gambia","Georgia","Germany"]
population = ["4,421,257", "1,249,397","77,540,650","847,706",
              "5,249,060","65,495,540","1,532,691","1,247,047",
              "4,576,303","82,695,290"]
contient = ["Africa", "Europe","Africa","Oceania","Europe",
            "Europe","Africa","Africa","Asia","Europe"]
areaKm2 = ["117,600", "45,100","1,104,300","18,274","338,145",
           "551,500","267,668","11,295","69,700","357,022"]
scrollbar = Scrollbar(window, orient=VERTICAL)
scrollbar.grid(row=1, column=1,rowspan=7, sticky=N+S+W)
listbox = Listbox(window,width=30,
                  height=10, yscrollcommand=scrollbar)
listbox.grid(row=1,column=0, rowspan=7)
scrollbar.config(command=listbox.yview)
for country in countries:
    listbox.insert('end', country)
contLabel = Label(window, text="Continent:")
contLabel.grid(row=1,column=2,sticky=N+S, pady=10)
popLabel = Label(window, text="Population:")
popLabel.grid(row=2,column=2,sticky=N+S)
areaLabel = Label(window, text="Area(km^2):")
areaLabel.grid(row=3,column=2,sticky=N+S)
cont = StringVar()
pop = StringVar()
area = StringVar()
outcont = Entry(window, state="readonly",justify=LEFT,textvariable= cont)
outcont.grid(row=1,column=3)
outPop = Entry(window, state="readonly",justify=LEFT,textvariable= pop)
outPop.grid(row=2,column=3)
outarea = Entry(window, state="readonly",justify=LEFT,textvariable= area)
outarea.grid(row=3,column=3)
listbox.bind("<<ListboxSelect>>", showInfo)
window.mainloop()
