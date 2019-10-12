import tkinter as tk
import requests

root = tk.Tk()

#INSERT CODE BELOW HERE VVVVVVVV

HEIGHT = 500
WIDTH = 500

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.place()

#Stall 1 Information
frame_1 = tk.Frame(root, bg='lightblue', bd=10)
frame_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_1 = tk.Label(frame_1, text="Welcome to Stall 1", font=("Courier", 10))
label_1.place(relwidth=1, relheight=1)

button_1 = tk.Button(frame_1, text = "Back", font=("Courier", 8), command=frame_1.lower)
button_1.place(relx=0, rely=0, relwidth=0.1, relheight=0.05)

#Stall 2 Information
frame_2 = tk.Frame(root, bg='lightblue', bd=10)
frame_2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_2 = tk.Label(frame_2, text="Welcome to Stall 2", font=("Courier", 10))
label_2.place(relwidth=1, relheight=1)

button_2 = tk.Button(frame_2, text = "Back", font=("Courier", 8), command=frame_2.lower)
button_2.place(relx=0, rely=0, relwidth=0.1, relheight=0.05)

#Stall 3 Information
frame_3 = tk.Frame(root, bg='lightblue', bd=10)
frame_3.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_3 = tk.Label(frame_3, text="Welcome to Stall 3", font=("Courier", 10))
label_3.place(relwidth=1, relheight=1)

button_3 = tk.Button(frame_3, text = "Back", font=("Courier", 8), command=frame_3.lower)
button_3.place(relx=0, rely=0, relwidth=0.1, relheight=0.05)

#Stall 4 Information
frame_4 = tk.Frame(root, bg='lightblue', bd=10)
frame_4.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_4 = tk.Label(frame_4, text="Welcome to Stall 4", font=("Courier", 10))
label_4.place(relwidth=1, relheight=1)

button_4 = tk.Button(frame_4, text = "Back", font=("Courier", 8), command=frame_4.lower)
button_4.place(relx=0, rely=0, relwidth=0.1, relheight=0.05)

##########################

background_image = tk.PhotoImage(file='food.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



button = tk.Button(root, text = "Stall 1", bd=5, command = frame_1.lift)
button.place(relx=0, rely=0.3, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 2", bd=5, command = frame_2.lift)
button.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 3", bd=5, command = frame_3.lift)
button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.2)

button = tk.Button(root, text = "Stall 4", bd=5, command = frame_4.lift)
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
