from tkinter import *
 
raam = Tk()
raam.title("Pärnu lipp")

tahvel = Canvas(raam, width=600, height = 300)
kõrgus = 75
i = 0
while i < 3:
    if i == 0 or i == 1:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 2) * kõrgus, fill="dodgerblue1", outline="dodgerblue1")
    else:
        tahvel.create_rectangle(0, i * kõrgus, 600, (i + 2) * kõrgus, fill="white", outline="white")

    i += 1
tahvel.pack()
raam.mainloop()