from tkinter import *
raam = Tk()
raam.title("Liiklusmärk 221")
tahvel = Canvas(raam, width=700, height = 600)
tahvel.create_polygon(50, 30, 650, 30, 350, 550, fill="white", width = 40, outline="red")
tahvel.pack()
raam.mainloop()