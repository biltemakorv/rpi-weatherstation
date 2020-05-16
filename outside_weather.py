import tkinter as tk
from font_select import FontSelection
from inside_weather import InsideWeather

from bs4 import BeautifulSoup
import requests
import re


class OutsideTemp(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.outside_temp = tk.Label(self, text="", font=FontSelection.size2(self))
        
        self.outside_temp.pack()  
        
        self.get_current()


    def get_current(self):
        #page_link_2 ='https://www.temperatur.nu/majelden.html'
        page_link_2 ='https://www.temperatur.nu/hagaberg.html'
        
        # fetch the content from url
        page_response_2 = requests.get(page_link_2, timeout=10)

        # parse html

        page_content_2 = BeautifulSoup(page_response_2.content, "html.parser")

        # extract all html elements where price is stored

        temp_now = page_content_2.find_all('span', attrs={'class':'favoritTemp'})

        #print(temp_now)

        dataRegex = re.compile(r'[+-]?\d+[,.]?\d+|[+-]?\d+')


        temp_now_result = dataRegex.findall(temp_now[0].get_text())
        temp_now_result_final = (temp_now_result[0].replace(",", "."))

        
        self.outside_temp.configure(text='{}'.format(temp_now_result_final))
  
        
        self.after(600000, self.get_current) #every 10minutes

class ForecastSummary(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.max_min = tk.Label(self, text="", font=FontSelection.size0(self))
        self.wind = tk.Label(self, text="", font=FontSelection.size0(self))
        self.precip = tk.Label(self, text="", font=FontSelection.size0(self))
        self.indoor_temp = InsideWeather(self) 
        
        self.max_min.pack()
        self.wind.pack()
        self.precip.pack()
        self.indoor_temp.pack()
        
        self.get_current()


    def get_current(self):
        page_link ='https://www.yr.no/en/forecast/daily-table/2-2694762/Sweden/%C3%96sterg%C3%B6tland/Link%C3%B6pings%20Kommun/Link%C3%B6ping'
        
       
        page_response = requests.get(page_link, timeout=10)

        # parse html
        page_content = BeautifulSoup(page_response.content, "html.parser")


        # extract all html elements where price is stored
        weather_today = page_content.find_all('li', attrs={'id':'dailyWeatherListItem0'})

        #print(temp_now)

        dataRegex = re.compile(r'[+-]?\d+[,.]?\d+|[+-]?\d+')

        weather_today_result = dataRegex.findall((weather_today[0].get_text()))
        
        self.max_min.configure(text='{} | {}'.format(weather_today_result[1], weather_today_result[2]))        
        self.precip.configure(text='{} mm'.format(weather_today_result[3])) 
        self.wind.configure(text='{} m/s'.format(weather_today_result[4]))     

        
        self.after(600000, self.get_current) #every 10minutes

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Weather Data")
    root.geometry('{}x{}'.format(800, 480)) 
    OutsideTemp(root).pack(side="top", fill="both", expand=True)
    ForecastSummary(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

