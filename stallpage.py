import tkinter as tk
from datetime import datetime
from tkinter import font
 
now = datetime.now()
current_date = now.strftime("%B %d, %Y  %H:%M:%S" )
h = 500
w = 700
 
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
 
root = tk.Tk()
 
#Stall 1
canvas = tk.Canvas(root, height = h, width = w)
canvas.pack()
 
stallphotoframe = tk.Frame(root, bg = "#AADDE7")
stallphotoframe.place(relx = 0.0, rely = 0.0, relheight = 0.5, relwidth = 0.5)
 
stallphotolabel = tk.Label(stallphotoframe, text = "Photo of Stall 1 insert here", fg = "black", bg = "white")
stallphotolabel.place(relx = 0.2, rely = 0.1, relheight = 0.6, relwidth = 0.6)
 
stallnamelabel = tk.Label(stallphotoframe, text = "Insert name of stall 1 here", fg = "black", bg = "white")
stallnamelabel.place(relx = 0.1, rely = 0.8, relheight = 0.1, relwidth = 0.8)
  
queue_frame = tk.Frame(root, bg = "#AADDE7")
queue_frame.place(relheight = 0.4, relwidth = 0.4, relx = 0.6, rely = 0.0)
 
wait_label = tk.Label(queue_frame, text = "WAIT TIME CALCULATOR", bg = "#AADDE7", font = ("Gill Sans MT Ext Condensed Bold", 20))
wait_label.place(relheight = 0.2, relwidth = 0.7, relx = 0.2, rely = 0.0)
 
queue_label = tk.Label(queue_frame, text = "Enter no. of pax in queue: ", fg = "black", bg = "#AADDE7")
queue_label.place(relheight = 0.2, relwidth = 0.5, relx = 0.1, rely = 0.2)
 
queue_entry = tk.Entry(queue_frame, bg = "white", fg = "black")
queue_entry.place(relheight = 0.1, relwidth = 0.4, relx = 0.1, rely = 0.4)
 
queue_button = tk.Button(queue_frame, text = "Calculate", fg = "white", bg = "#029A64", command=lambda : get_queue_time(queue_entry.get()))
queue_button.place(relheight = 0.1, relwidth = 0.3, relx = 0.6, rely = 0.4)
 
queue_time_output = tk.Label(queue_frame, bg = 'white', fg = 'black')
queue_time_output.place(relheight = 0.2, relwidth = 0.8, relx = 0.5, rely = 0.6, anchor = 'n')
 
bottom_frame = tk.Frame(root, bg = "#AADDE7")
 
bottom_frame.place(relheight = 0.05, relwidth = 1.0, relx = 0.0, rely = 0.95)
 
date_label = tk.Label(bottom_frame, text = current_date, fg = "black", bg = "#AADDE7" )
date_label.place(relheight = 0.5, relwidth = 0.5, relx = 0.25, rely = 0.1)
 
back_button = tk.Button(stallphotoframe, text = "Back", fg = "white", bg = "#029A64")
back_button.place(relheight = 0.1, relwidth = 0.2, relx = 0.0, rely = 0.0)
 
normal_menu_frame = tk.Frame(root, bg = "#AADDE7")
normal_menu_frame.place(relheight = 0.4, relwidth = 0.5, relx = 0.0, rely = 0.525)
 
normal_menu_title = tk.Label(normal_menu_frame, text = "MENU", bg = "#AADDE7", font = ("Gill Sans MT Ext Condensed Bold", 20))
normal_menu_title.place(relheight = 0.2, relwidth = 0.2, relx = 0.4, rely = 0.0)
 
special_meal_frame = tk.Frame(root, bg = "#AADDE7")
special_meal_frame.place(relheight = 0.4, relwidth = 0.4, relx = 0.6, rely = 0.525, anchor = 'nw' )
 
special_meal_title = tk.Label(special_meal_frame, text = 'Meal of the Day', fg = "black", bg = "#AADDE7",font = ("Gill Sans MT Ext Condensed Bold", 20))
special_meal_title.place(relheight = 0.2, relwidth = 0.4, relx = 0.5, rely = 0.0, anchor = 'n')
 
special_meal_of_day = tk.Label(special_meal_frame, bg = 'white', fg = 'black', text = weekday + ' : ' + special_meal[weekday.lower()])
special_meal_of_day.place(relheight = 0.7, relwidth = 0.8, anchor = 'nw', relx = 0.1, rely = 0.2)
 
root.mainloop()
