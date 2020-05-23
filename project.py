from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#import sqlite3
#connect = sqlite3.connect('users.db')
#cursor = connect.cursor()
#cursor.execute('CREATE TABLE IF NOT EXISTS users (login text) ')
#connect.commit()
#connect.close()

class MainWindow(Screen):
    pass

class WeatherWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("one.kv")


class MyMainApp(App):
    def build(self):
        return kv


MyMainApp().run()

