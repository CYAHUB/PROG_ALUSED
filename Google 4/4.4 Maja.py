from tkinter import *
raam = Tk()
raam.title("Maja")

tahvel = Canvas(raam, width=600, height = 600)
tahvel.create_rectangle(0, 0, 600,600, fill="dodgerblue1", outline="dodgerblue1")
tahvel.create_rectangle(600, 599, 0,500, fill="yellow", outline="yellow")
tahvel.create_rectangle(450, 200, 425,400, fill="purple", outline="purple")
tahvel.create_oval(225, 300, 500,500, fill="azure4", outline="azure4")
tahvel.create_rectangle(500, 400, 225,500, fill="brown", outline="brown")

tahvel.pack()
raam.mainloop()



