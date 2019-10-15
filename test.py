import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Welcome(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Welcome to NTU Canteen App")
       label.pack(side="top", fill="both", expand=True)

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
    
       stallphotoframe = tk.Frame(self, bg = "#AADDE7")
       stallphotoframe.place(relx = 0.0, rely = 0.0, relheight = 0.5, relwidth = 0.5)
    
       stallphotolabel = tk.Label(stallphotoframe, text = "Photo of Stall 1 insert here", fg = "black", bg = "white")
       stallphotolabel.place(relx = 0.2, rely = 0.1, relheight = 0.6, relwidth = 0.6)
    
       stallnamelabel = tk.Label(stallphotoframe, text = "Insert name of stall 1 here", fg = "black", bg = "white")
       stallnamelabel.place(relx = 0.1, rely = 0.8, relheight = 0.1, relwidth = 0.8)
    
       queue_frame = tk.Frame(self, bg = "#AADDE7")
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
    
       bottom_frame = tk.Frame(self, bg = "#AADDE7")
       bottom_frame.place(relheight = 0.05, relwidth = 1.0, relx = 0.0, rely = 0.95)
    
       date_label = tk.Label(bottom_frame, text = "current_date", fg = "black", bg = "#AADDE7" )
       date_label.place(relheight = 0.5, relwidth = 0.5, relx = 0.25, rely = 0.1)
    
       back_button = tk.Button(stallphotoframe, text = "Back", fg = "white", bg = "#029A64")
       back_button.place(relheight = 0.1, relwidth = 0.2, relx = 0.0, rely = 0.0)
    
       normal_menu_frame = tk.Frame(self, bg = "#AADDE7")
       normal_menu_frame.place(relheight = 0.4, relwidth = 0.5, relx = 0.0, rely = 0.525)
    
       normal_menu_title = tk.Label(normal_menu_frame, text = "MENU", bg = "#AADDE7", font = ("Gill Sans MT Ext Condensed Bold", 20))
       normal_menu_title.place(relheight = 0.2, relwidth = 0.2, relx = 0.4, rely = 0.0)
    
       special_meal_frame = tk.Frame(self, bg = "#AADDE7")
       special_meal_frame.place(relheight = 0.4, relwidth = 0.4, relx = 0.6, rely = 0.525, anchor = 'nw' )
    
       special_meal_title = tk.Label(special_meal_frame, text = 'Meal of the Day', fg = "black", bg = "#AADDE7",font = ("Gill Sans MT Ext Condensed Bold", 20))
       special_meal_title.place(relheight = 0.2, relwidth = 0.4, relx = 0.5, rely = 0.0, anchor = 'n')
    
       special_meal_of_day = tk.Label(special_meal_frame, bg = 'white', fg = 'black', text = "weekday" + ' : ' + "special_meal[weekday.lower()]")
       special_meal_of_day.place(relheight = 0.7, relwidth = 0.8, anchor = 'nw', relx = 0.1, rely = 0.2)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       stallphotoframe = tk.Frame(self, bg = "#AADDE7")
       stallphotoframe.place(relx = 0.0, rely = 0.0, relheight = 0.5, relwidth = 0.5)
    
       stallphotolabel = tk.Label(stallphotoframe, text = "Photo of Stall 2 insert here", fg = "black", bg = "white")
       stallphotolabel.place(relx = 0.2, rely = 0.1, relheight = 0.6, relwidth = 0.6)
    
       stallnamelabel = tk.Label(stallphotoframe, text = "Insert name of stall 2 here", fg = "black", bg = "white")
       stallnamelabel.place(relx = 0.1, rely = 0.8, relheight = 0.1, relwidth = 0.8)
    
       queue_frame = tk.Frame(self, bg = "#AADDE7")
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
    
       bottom_frame = tk.Frame(self, bg = "#AADDE7")
       bottom_frame.place(relheight = 0.05, relwidth = 1.0, relx = 0.0, rely = 0.95)
    
       date_label = tk.Label(bottom_frame, text = "current_date", fg = "black", bg = "#AADDE7" )
       date_label.place(relheight = 0.5, relwidth = 0.5, relx = 0.25, rely = 0.1)
    
       back_button = tk.Button(stallphotoframe, text = "Back", fg = "white", bg = "#029A64")
       back_button.place(relheight = 0.1, relwidth = 0.2, relx = 0.0, rely = 0.0)
    
       normal_menu_frame = tk.Frame(self, bg = "#AADDE7")
       normal_menu_frame.place(relheight = 0.4, relwidth = 0.5, relx = 0.0, rely = 0.525)
    
       normal_menu_title = tk.Label(normal_menu_frame, text = "MENU", bg = "#AADDE7", font = ("Gill Sans MT Ext Condensed Bold", 20))
       normal_menu_title.place(relheight = 0.2, relwidth = 0.2, relx = 0.4, rely = 0.0)
    
       special_meal_frame = tk.Frame(self, bg = "#AADDE7")
       special_meal_frame.place(relheight = 0.4, relwidth = 0.4, relx = 0.6, rely = 0.525, anchor = 'nw' )
    
       special_meal_title = tk.Label(special_meal_frame, text = 'Meal of the Day', fg = "black", bg = "#AADDE7",font = ("Gill Sans MT Ext Condensed Bold", 20))
       special_meal_title.place(relheight = 0.2, relwidth = 0.4, relx = 0.5, rely = 0.0, anchor = 'n')
    
       special_meal_of_day = tk.Label(special_meal_frame, bg = 'white', fg = 'black', text = "weekday" + ' : ' + "special_meal[weekday.lower()]")
       special_meal_of_day.place(relheight = 0.7, relwidth = 0.8, anchor = 'nw', relx = 0.1, rely = 0.2)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       stallphotoframe = tk.Frame(self, bg = "#AADDE7")
       stallphotoframe.place(relx = 0.0, rely = 0.0, relheight = 0.5, relwidth = 0.5)
    
       stallphotolabel = tk.Label(stallphotoframe, text = "Photo of Stall 3 insert here", fg = "black", bg = "white")
       stallphotolabel.place(relx = 0.2, rely = 0.1, relheight = 0.6, relwidth = 0.6)
    
       stallnamelabel = tk.Label(stallphotoframe, text = "Insert name of stall 3 here", fg = "black", bg = "white")
       stallnamelabel.place(relx = 0.1, rely = 0.8, relheight = 0.1, relwidth = 0.8)
    
       queue_frame = tk.Frame(self, bg = "#AADDE7")
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
    
       bottom_frame = tk.Frame(self, bg = "#AADDE7")
       bottom_frame.place(relheight = 0.05, relwidth = 1.0, relx = 0.0, rely = 0.95)
    
       date_label = tk.Label(bottom_frame, text = "current_date", fg = "black", bg = "#AADDE7" )
       date_label.place(relheight = 0.5, relwidth = 0.5, relx = 0.25, rely = 0.1)
    
       back_button = tk.Button(stallphotoframe, text = "Back", fg = "white", bg = "#029A64")
       back_button.place(relheight = 0.1, relwidth = 0.2, relx = 0.0, rely = 0.0)
    
       normal_menu_frame = tk.Frame(self, bg = "#AADDE7")
       normal_menu_frame.place(relheight = 0.4, relwidth = 0.5, relx = 0.0, rely = 0.525)
    
       normal_menu_title = tk.Label(normal_menu_frame, text = "MENU", bg = "#AADDE7", font = ("Gill Sans MT Ext Condensed Bold", 20))
       normal_menu_title.place(relheight = 0.2, relwidth = 0.2, relx = 0.4, rely = 0.0)
    
       special_meal_frame = tk.Frame(self, bg = "#AADDE7")
       special_meal_frame.place(relheight = 0.4, relwidth = 0.4, relx = 0.6, rely = 0.525, anchor = 'nw' )
    
       special_meal_title = tk.Label(special_meal_frame, text = 'Meal of the Day', fg = "black", bg = "#AADDE7",font = ("Gill Sans MT Ext Condensed Bold", 20))
       special_meal_title.place(relheight = 0.2, relwidth = 0.4, relx = 0.5, rely = 0.0, anchor = 'n')
    
       special_meal_of_day = tk.Label(special_meal_frame, bg = 'white', fg = 'black', text = "weekday" + ' : ' + "special_meal[weekday.lower()]")
       special_meal_of_day.place(relheight = 0.7, relwidth = 0.8, anchor = 'nw', relx = 0.1, rely = 0.2)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        w = Welcome(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        b1 = tk.Button(buttonframe, text = "Stall 1", bd=5, command=p1.lift)
        b1.pack(side="left")

        b2 = tk.Button(buttonframe, text = "Stall 2", bd=5, command=p2.lift)
        b2.pack(side="left")

        b3 = tk.Button(buttonframe, text = "Stall 3", bd=5, command=p3.lift)
        b3.pack(side="left")

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        w.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        w.show()



if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()