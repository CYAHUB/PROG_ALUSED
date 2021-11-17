from tkinter import *
 
raam = Tk()
raam.title("4.3 Liiklusmärk")

tahvel = Canvas(raam, width=300, height = 300)
tahvel.create_oval(0, 0, 300,300, fill="red", outline="red")
tahvel.create_oval(25, 25, 275,275, fill="white", outline="white")

tahvel.pack()
raam.mainloop()
