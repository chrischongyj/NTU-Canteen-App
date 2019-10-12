import tkinter as tk
import requests

root = tk.Tk()

#INSERT CODE BELOW HERE VVVVVVVV

HEIGHT = 500
WIDTH = 500

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.place()

background_image = tk.PhotoImage(file='food.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(root, text = "Stall 1", bd=5)
button.place(relx=0, rely=0.3, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 2", bd=5)
button.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 3", bd=5)
button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 4", bd=5)
button.place(relx=0.75, rely=0.3, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 5", bd=5)
button.place(relx=0, rely=0.55, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 6", bd=5)
button.place(relx=0.25, rely=0.55, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 7", bd=5)
button.place(relx=0.5, rely=0.55, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 8", bd=5)
button.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.2)



canvas_2 = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

canvas_3 = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

canvas_4 = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()




#INSERT CODE ABOVE HERE ^^^^^^^^


root.mainloop()
