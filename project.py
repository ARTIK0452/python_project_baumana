from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import requests

#import sqlite3
#connect = sqlite3.connect('users.db')
#cursor = connect.cursor()
#cursor.execute('CREATE TABLE IF NOT EXISTS users (login text) ')
#connect.commit()
#connect.close()

class MainWindow(Screen):
    pass

class WeatherWindow(Screen):
    def search_info_weather(self, requests):
        listKey = ['weather']
        s_city = self.cityCountry.text
        appid = "5d9d9f7178756dbc78d68958da985841"
        if self.search.on_release:
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/find",
                    params={'q': self.s_city, 'APPID': appid})
                data = res.json()
                for k, v in data['list'][1].items():
                    print(k, v)
            except Exception as e:
                self.infoweater.text = e 

class InfoWeather(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("one.kv")

class MyMainApp(App):
    def build(self):
        return kv      

MyMainApp().run()
