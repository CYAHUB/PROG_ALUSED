from tkinter import *
 
raam = Tk()
raam.title("Male")

tahvel = Canvas(raam, width=400, height = 400)

# background
tahvel.create_rectangle(0, 0, 1000,1000, fill="White", outline="White")

# Line 1
tahvel.create_rectangle(0, 0, 50,50, fill="Black", outline="Black")
tahvel.create_rectangle(0, 150, 50,100, fill="Black", outline="Black")
tahvel.create_rectangle(0, 250, 50,200, fill="Black", outline="Black")
tahvel.create_rectangle(0, 350, 50,300, fill="Black", outline="Black")

# Line 2
tahvel.create_rectangle(50, 50, 100,100, fill="Black", outline="Black")
tahvel.create_rectangle(50, 200, 100,150, fill="Black", outline="Black")
tahvel.create_rectangle(50, 300, 100,250, fill="Black", outline="Black")
tahvel.create_rectangle(50, 400, 100,350, fill="Black", outline="Black")

# Line 3
tahvel.create_rectangle(100, 0, 150,50, fill="Black", outline="Black")
tahvel.create_rectangle(100, 100, 150,150, fill="Black", outline="Black")
tahvel.create_rectangle(100, 200, 150,250, fill="Black", outline="Black")
tahvel.create_rectangle(100, 300, 150,350, fill="Black", outline="Black")

# Line 4
tahvel.create_rectangle(150, 50, 200,100, fill="Black", outline="Black")
tahvel.create_rectangle(150, 150, 200,200, fill="Black", outline="Black")
tahvel.create_rectangle(150, 250, 200,300, fill="Black", outline="Black")
tahvel.create_rectangle(150, 350, 200,400, fill="Black", outline="Black")

# Line 5
tahvel.create_rectangle(200, 0, 250,50, fill="Black", outline="Black")
tahvel.create_rectangle(200, 100, 250,150, fill="Black", outline="Black")
tahvel.create_rectangle(200, 200, 250,250, fill="Black", outline="Black")
tahvel.create_rectangle(200, 300, 250,350, fill="Black", outline="Black")

# Line 6
tahvel.create_rectangle(250, 50, 300,100, fill="Black", outline="Black")
tahvel.create_rectangle(250, 150, 300,200, fill="Black", outline="Black")
tahvel.create_rectangle(250, 250, 300,300, fill="Black", outline="Black")
tahvel.create_rectangle(250, 350, 300,400, fill="Black", outline="Black")

# Line 7
tahvel.create_rectangle(300, 0, 350,50, fill="Black", outline="Black")
tahvel.create_rectangle(300, 100, 350,150, fill="Black", outline="Black")
tahvel.create_rectangle(300, 200, 350,250, fill="Black", outline="Black")
tahvel.create_rectangle(300, 300, 350,350, fill="Black", outline="Black")

# Line 8
tahvel.create_rectangle(350, 50, 400,100, fill="Black", outline="Black")
tahvel.create_rectangle(350, 150, 400,200, fill="Black", outline="Black")
tahvel.create_rectangle(350, 250, 400,300, fill="Black", outline="Black")
tahvel.create_rectangle(350, 350, 400,400, fill="Black", outline="Black")

tahvel.pack()
raam.mainloop()
