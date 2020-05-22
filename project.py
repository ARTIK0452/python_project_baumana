from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label


#from vk_api import vk_api
	
class EnterAccountWindow(Screen):
	pass
	#self.user = input('number phone: ')
	#self.passw = input('password: ')
	#def __init__(self, user, passw):
		#vk_session = vk_api.VkApi(str(user), str(passw))
		#vk_session.auth()
		#vk = vk_session.get_api()
		#print('userID: ', vk_session.token['user_id'])

class MainWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass

kv = Builder.load_file("login.kv")

class MyProjectApp(App):
	def build(self):
		return kv
	       
MyProjectApp().run()

