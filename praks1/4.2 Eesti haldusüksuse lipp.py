from tkinter import *

raam = Tk()
raam.title("Aseri valla lipp")
tahvel = Canvas(raam, width=600, height = 400)
tahvel.create_rectangle(0, 0, 600, 150, fill="dark blue")
tahvel.create_rectangle(0, 150, 600, 250, fill="white")
tahvel.create_rectangle(0, 250, 600, 400, fill="green")
tahvel.pack()
raam.mainloop()