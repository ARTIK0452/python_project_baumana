import math
import datetime
import weatherTest
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app	import MDApp, App
from kivymd.theming import ThemableBehavior
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from kivymd.uix.behaviors import TouchBehavior
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
import sqlite3

#connect = sqlite3.connect('search_history.db')

KV = '''
<ContentNavigationDrawer>:
    ScrollView:
        MDList:

            OneLineListItem:
                text: "Weather"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "weather"

            OneLineListItem:
                text: "History"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "history"

            OneLineListItem:
                text: "Settings"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "settings"

            OneLineListItem:
                text: "About"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "about_me"


Screen:
    
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Open Weather"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            name: screen_manager

            Screen:
                id: screen1
                name: "weather"
                #canvas.before:
                    #Rectangle:
                        #id: rectangle1
                        #pos: self.pos
                        #size: self.size
                        #source: 'clouds.png'

                textinput: textinput
                search: search
                cError: cError

                dateTime: dateTime
                timeZone: timeZone
                
                MDTextField:
                    id: textinput
                    size_hint: .54, .1
                    pos_hint: {'x': .2, 'y': .75}
                    hint_text: "Введите город для поиска"
                MyButton:
                    id: search
                    name: textinput.text
                    size_hint: .54, .08
                    pos_hint: {'x':.2, 'y': .67}
                    text: 'Поиск'
                    
                MDGridLayout:
                    id: mdgridweather
                    adaptive_height: True
                    cols: 2
                    rows: 13
                    pos_hint: {'x':.17,'y': 0.01}
                    col_default_width: '340dp'
                    col_force_default: True
                    spacing: 10, 30
                    MDLabel:
                        id: tError
                        color: 1,0,1,1
                        text: ""
                    MDLabel:
                        id: cError
                        color: 1,0,1,1
                        text: ""
                    MDLabel:
                        text: "Дата, время"
                    MDLabel:
                        id: dateTime
                        text: "*"
                    MDLabel:
                        name:
                        text: "Город"
                    MDLabel:
                        id: cityName
                        text: "*"
                    MDLabel:
                        name:
                        text: "Временная зона"
                    MDLabel:
                        id: timeZone
                        text: "*"
                    MDLabel:
                        text: "Актуальная температура"
                    MDLabel:
                        id: CurrentTemperature
                        text: "*"
                    MDLabel:
                        text: "Влажность воздуха"
                    MDLabel:
                        id: AirHumidity
                        text: "*"
                    MDLabel:
                        text: "Давление"
                    MDLabel:
                        id: Pressure
                        text: "*"
                    MDLabel:
                        text: "Облачность"
                    MDLabel:
                        id: Cloudiness
                        text: "*"
                    MDLabel:
                        text: "Скорость ветра"
                    MDLabel:
                        id: windSpeed
                        text: "*"
                    MDLabel:
                        text: "Направление ветра"
                    MDLabel:
                        id: windDirection
                        text: "*"
                    MDLabel:
                        text: "Описание"
                    MDLabel:
                        id: description
                        text: "*"
                    
                        
                    
                    
            Screen:
                name: "history"
                MDGridLayout:
                    cols: 1
                    MDLabel:
                        id: noy
                        text: "Здесь пока пусто!"
                        halign: "center"

            Screen:
                name: "settings"
                MDLabel:
                    text: "settings"
                    halign: "center"

            Screen:
                name: "about_me"
                MDLabel:
                    id: cError
                    pos_hint: {'y': .3}
                    text: "Powered by inginerium"
                    halign: "center"
                MDLabel:
                    id: cError
                    pos_hint: {'y': .2}
                    text: "Тоже что-то написанно..."
                    halign: "center"
                MDLabel:
                    id: cError
                    pos_hint: {'y': .1}
                    text: "Созданно с помощью бесплатного api от Open Weather"
                    halign: "center"
                MDLabel:
                    id: cError
                    pos_hint: {'y': .01}
                    text: "Разработчик: Валов Артур"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class myclass(MDLabel):
    def putData(self):
        print(MDLabel.ids.cityCountry.text)

class MyButton(MDRoundFlatButton, ThemableBehavior):
    #def insert_db(self, nscity):
        #try:
            #print(nscity)
            #connect = sqlite3.connect('history_weather.db')
            #cursor = connect.cursor()
            #cursor.execute('''CREATE TABLE history (city text)''')
            #c.execute("INSERT INTO history (city) VALUES ("{nscity}")")
            #connect.commit()
        #except:
            #print('govno')

    def on_release(self, *args):
        
        app = App.get_running_app()
        app.root.ids['tError'].text = ''
        app.root.ids['cError'].text = ''
        #app.root.ids['mdgridweather'].canvas.clear()
        #app.root.ids['screen1'].canvas = Rectangle(source='blue.png', pos=self.pos, size=self.size)
        my = weatherTest.getWeather(self.name)
        listWeather = my.geo_location()
        if listWeather:
            #self.insert_db(self.name)
            ssh = str(listWeather[0]).split('.')
            if len(ssh) == 1:
                ssh.append(0)
            vdg = str(listWeather[1]).split('.')
            if len(vdg) == 1:
                vdg.append(0)
            
            app.root.ids['dateTime'].text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            app.root.ids['cityName'].text = self.name + ' ' + str(ssh[0]) + '°' + str(ssh[1]) + "'" + ' с. ш.' + ' ' + str(vdg[0]) + '°' + str(vdg[1]) + "'" + ' в. д.'
            if listWeather[8] == '180':
                windD = 'Южный'
            elif listWeather[8] == '90':
                windD = 'Восточный'
            elif listWeather[8] == '360':
                windD = 'Северный'
            elif listWeather[8] == '270':
                windD = 'Западный'
            elif 0 < listWeather[8] < 90:
                windD = 'Северо-восточный'
            elif 90 < listWeather[8] < 180:
                windD = 'Юго-восточный'
            elif 180 < listWeather[8] < 270:
                windD = 'Юго-западный'
            elif 270 < listWeather[8] < 360:
                windD = 'Северо-западный'
            
            
            try:
                app.root.ids['timeZone'].text = listWeather[2]
            except:
                app.root.ids['timeZone'].text = 'нет данных'
            try:
                app.root.ids['CurrentTemperature'].text = str(listWeather[3]) + ' °C'
            except:
                app.root.ids['CurrentTemperature'].text = 'нет данных'
            try:
                app.root.ids['Pressure'].text = str(listWeather[4]*0.75) + ' мм рт.ст.'
            except:
                app.root.ids['Pressure'].text = 'нет данных'
            try:
                app.root.ids['AirHumidity'].text = str(listWeather[5]) + ' %'
            except:
                app.root.ids['AirHumidity'].text = 'нет данных'
            try:
                app.root.ids['Cloudiness'].text = str(listWeather[6]) + ' %'
            except:
                app.root.ids['Cloudiness'].text = 'нет данных'
            try:
                app.root.ids['windSpeed'].text = str(listWeather[7]) + ' м/с'
            except:
                app.root.ids['windSpeed'].text = 'нет данных'
            try:
                app.root.ids['windDirection'].text = str(listWeather[8]) + '° - ' + windD
            except:
                app.root.ids['windDirection'].text = 'нет данных'
            try:
                app.root.ids['description'].text = str(listWeather[9])
            except:
                app.root.ids['description'].text = 'нет данных'
            
        else:
            app.root.ids['tError'].text = 'Ошибка'
            app.root.ids['cError'].text = 'Нет сети или города'
            app.root.ids['dateTime'].text = 'нет данных'
            app.root.ids['cityName'].text = 'нет данных'
            app.root.ids['timeZone'].text = 'нет данных'
            app.root.ids['CurrentTemperature'].text = 'нет данных'
            app.root.ids['Pressure'].text = 'нет данных'
            app.root.ids['AirHumidity'].text = 'нет данных'
            app.root.ids['Cloudiness'].text = 'нет данных'
            app.root.ids['windSpeed'].text = 'нет данных'
            app.root.ids['windDirection'].text = 'нет данных'
            app.root.ids['description'].text = 'нет данных'
            
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class OpenWeather(MDApp):
    def build(self):
        return Builder.load_string(KV)
   
            

OpenWeather().run()
