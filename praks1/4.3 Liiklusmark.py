from tkinter import *
raam = Tk()
raam.title("Liiklusmärk 221")
tahvel = Canvas(raam, width=700, height = 600)
tahvel.create_polygon(0, 0, 700, 0, 350, 600, fill="red",)
tahvel.create_polygon(50, 30, 650, 30, 350, 550, fill="white",)
tahvel.pack()
raam.mainloop()