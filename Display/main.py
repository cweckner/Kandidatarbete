from kivymd.app import MDApp
from screen_nav import sc_helper
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.picker import MDTimePicker, MDDatePicker



class WelcomeScreen(Screen):
    pass

class InputScreen(Screen):
    pass

class GoodbyeScreen(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(WelcomeScreen(name = 'welcome'))
screen_manager.add_widget(InputScreen(name = 'inputs'))
screen_manager.add_widget(GoodbyeScreen(name = 'goodbye'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(sc_helper)  
        return screen

    def show_time_picker(self):
        '''Open time picker dialog.'''

        time_dialog = MDTimePicker()
        time_dialog.open()

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

#if self.username.text == "admin":
#           root.manager.current = 'inputs'

DemoApp().run()


