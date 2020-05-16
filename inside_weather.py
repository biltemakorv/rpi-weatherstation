import tkinter as tk
from font_select import FontSelection

from w1thermsensor import W1ThermSensor


class InsideWeather(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)



        self.indoor_temp = tk.Label(self, text="", font=FontSelection.size0(self))
        self.indoor_temp.pack()

        self.read_temp()

 
    def read_temp(self):
        self.sensor = W1ThermSensor()
        self.temperature = self.sensor.get_temperature()
        self.temperature = round(self.temperature,1)


        self.indoor_temp.configure(text='{}'.format(self.temperature))
        self.after(1000, self.read_temp)
        


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Home temprature")
    root.geometry('{}x{}'.format(800, 240)) 
    InsideWeather(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

