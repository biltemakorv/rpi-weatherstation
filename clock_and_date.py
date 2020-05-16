import tkinter as tk
from font_select import FontSelection

import time

class Clock(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.timenow = tk.Label(self, text="", font=FontSelection.size3(self))
        self.timenow.pack()
        self.update_clock()
   
    def update_clock(self):
        now = time.strftime("%H:%M")

        self.timenow.configure(text='{}'.format(now))
        self.after(1000, self.update_clock)

class Date(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.datenow = tk.Label(self, text="", font=FontSelection.size0(self))
        self.datenow.pack()
        self.update_date()     

    def update_date(self):
        day = time.strftime("%A")
        date = time.strftime("%d %b")
        self.datenow.configure(text='{}\n{}'.format(day,date))
        self.after(1000, self.update_date)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Time and Date")
    root.geometry('{}x{}'.format(800, 480)) 
    Clock(root).pack(side="top", fill="both", expand=True)
    Date(root).pack(side="top", fill="both", expand=True)

    root.mainloop()

