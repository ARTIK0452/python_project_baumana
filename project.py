from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from vk_api import vk_api

class vk():
	user = input('number phone: ')
	passw = input('password: ')
	def __init__(self, user, passw):
		self.vk_session = vk_api.VkApi(str(user), str(passw))
		self.vk_session.auth()
		self,vk = vk_session.get_api()
		print('userID: ', vk_session.token['user_id'])
	
class MainWindow(Screen):
	pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('prog.kv')

class MyProjectApp(App):
    def build(self):
        return kv
	
        
        
MyProjectApp().run()


