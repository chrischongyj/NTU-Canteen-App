import tkinter as tk
import requests
from datetime import datetime
from stallpage import change_page

root = tk.Tk()

#INSERT CODE BELOW HERE VVVVVVVV

now = datetime.now()
current_date = now.strftime("%B %d, %Y  %H:%M:%S" )

current_time = datetime.now()
weekday = current_time.strftime('%A')
 
special_meal = {
    'monday' : 'meal1',
    'tuesday' : 'meal2',
    'wednesday' : 'meal3',
    'thursday' : 'meal4',
    'friday' : 'meal5',
    'saturday' : 'meal6',
    'sunday' : 'meal7'
}
    
 
def get_queue_time(queue_entry):
    queue_time = int(queue_entry)*2
    queue_time_output['text'] = 'The estimated queue time is: ' + str(queue_time) + ' min'



HEIGHT = 500
WIDTH = 500

#canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
#canvas.place()

background_image = tk.PhotoImage(file='food.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


button = tk.Button(root, text = "Stall 1", bd=5,command=lambda: change_page())
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

#INSERT CODE ABOVE HERE ^^^^^^^^


root.mainloop()
