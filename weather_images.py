import tkinter as tk


class Images(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        
        max_min_icon = tk.PhotoImage(file="/home/pi/Desktop/Temp_time_v1/img/icon-temperature.png")
        precip_icon = tk.PhotoImage(file="/home/pi/Desktop/Temp_time_v1/img/icon-precipitation.png")
        wind_icon = tk.PhotoImage(file="/home/pi/Desktop/Temp_time_v1/img/icon-wind.png")  
        house_icon = tk.PhotoImage(file="/home/pi/Desktop/Temp_time_v1/img/icon-house.png")    
        
        self.max_min = tk.Label(self, image=max_min_icon)
        self.precip = tk.Label(self, image=precip_icon)
        self.wind = tk.Label(self, image=wind_icon)
        self.house = tk.Label(self, image=house_icon)

        self.max_min.image = max_min_icon
        self.precip.image = precip_icon
        self.wind.image = wind_icon
        self.house.image = house_icon
        
        
        self.max_min.pack()
        self.wind.pack()
        self.precip.pack()
        self.house.pack()

     
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Images")
    root.geometry('{}x{}'.format(800, 480)) #screen size = 800x480'
    #root.attributes('-zoomed', True)

    Images(root).pack()
    root.mainloop()