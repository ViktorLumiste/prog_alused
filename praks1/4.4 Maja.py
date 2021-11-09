from tkinter import *

raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=600, height = 400, background="light blue")
tahvel.create_rectangle( 0, 300, 600, 400, fill="green" )
tahvel.create_rectangle( 80, 180, 520, 360, fill="orange")
tahvel.create_rectangle( 120, 240, 180, 360, fill = "#654321")
tahvel.create_rectangle( 300, 220, 380, 300, fill= "white")
tahvel.create_line(340, 220, 340, 300, width = 4, fill = "black")
tahvel.create_line(300, 260, 380, 260, width = 4, fill = "black")
tahvel.create_polygon( 80, 180, 300, 60, 520, 180, fill = "brown" )
tahvel.pack()
raam.mainloop()