from kivymd.app import MDApp
from screen_nav import sc_helper
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton



class WelcomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class InputScreen(Screen):
    pass



screen_manager = ScreenManager()
screen_manager.add_widget(WelcomeScreen(name = 'welcome'))
screen_manager.add_widget(LoginScreen(name = 'login'))
screen_manager.add_widget(InputScreen(name = 'inputs'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(sc_helper)  
        return screen

#if self.username.text == "admin":
#           root.manager.current = 'inputs'

DemoApp().run()