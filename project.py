from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import requests

class MainWindow(Screen):
    pass

class WeatherWindow(Screen):
    def search_info_weather(self, cct):
        listKey = ['weather']
        #self.s_city = self.cityCountry.text
        self.appid = "5d9d9f7178756dbc78d68958da985841"
        if self.search.on_release:
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/find",
                    params={'q': cct, 'APPID': self.appid})
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
