#! /usr/bin/python3

import tkinter as tk
from clock_and_date import Clock, Date
from outside_weather import OutsideTemp, ForecastSummary
from weather_images import Images
from hardware_screen import HardwareScreen

class Application(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        HardwareScreen.brightness(self)

        self.top_frame = tk.Frame(self)
        self.top_right = tk.Frame(self.top_frame, padx=35)
        self.top_left = tk.Frame(self.top_frame)

        self.bottom_frame = tk.Frame(self)
        self.bottom_right = tk.Frame(self.bottom_frame)
        self.bottom_left = tk.Frame(self.bottom_frame)

        self.outside = OutsideTemp(self.top_left)
        self.images = Images(self.top_right)
        self.summary = ForecastSummary(self.top_right)
        self.timenow = Clock(self.bottom_right) 
        self.datenow = Date(self.bottom_left)
        

        self.top_frame.pack(side=tk.TOP, fill='x')
        self.top_left.pack(side=tk.LEFT)
        self.top_right.pack(side=tk.RIGHT)
        
        self.bottom_frame.pack(side=tk.BOTTOM, fill='x')
        self.bottom_left.pack(side=tk.LEFT)
        self.bottom_right.pack(side=tk.RIGHT)
        
        self.outside.pack(side=tk.LEFT)
        self.images.pack(side=tk.LEFT, ipady=3)
        self.summary.pack(side=tk.LEFT)
        
        self.datenow.pack(side=tk.LEFT)
        self.timenow.pack(side=tk.LEFT)      


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Time and weather")
    root.geometry('{}x{}'.format(800, 480)) #screen size = 800x480
    root.attributes('-zoomed', True)

    Application(root).pack()
    root.mainloop()