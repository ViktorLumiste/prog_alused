from tkinter import *

raam = Tk()
raam.title("Aseri valla lipp")
tahvel = Canvas(raam, width=600, height = 400)
tahvel.create_rectangle(, , , , )
tahvel.create_rectangle( , , , , )
tahvel.create_polygon(, , , ,)
tahvel.pack()
raam.mainloop()