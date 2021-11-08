from tkinter import *

raam = Tk()
raam.title("Aseri valla lipp")
tahvel = Canvas(raam, width=600, height = 500)
tahvel.create_rectangle(0, 0, 600, 200, fill="blue")
tahvel.create_rectangle(0, 200, 600, 300, fill="white")
tahvel.create_rectangle(0, 300, 600, 500, fill="green")
tahvel.pack()
raam.mainloop()