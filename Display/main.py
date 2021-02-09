from kivymd.app import MDApp
from screen_nav import sc_helper
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.picker import MDTimePicker, MDDatePicker




class WelcomeScreen(Screen):
    pass

class InputScreen(Screen):
    pass

class CurrentChargeScreen(Screen):
    pass

class WantedChargeScreen(Screen):
    pass

class TimeDateScreen(Screen):
    pass

class BatteryCapacityScreen(Screen):
    pass

class MaxCurrentScreen(Screen):
    pass

class OutletScreen(Screen):
    pass

class GoodbyeScreen(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(WelcomeScreen(name = 'welcome'))
screen_manager.add_widget(InputScreen(name = 'inputs'))
screen_manager.add_widget(CurrentChargeScreen(name = 'currentcharge'))
screen_manager.add_widget(WantedChargeScreen(name = 'wantedcharge'))
screen_manager.add_widget(TimeDateScreen(name = 'timedate'))
screen_manager.add_widget(BatteryCapacityScreen(name = 'batterycapacity'))
screen_manager.add_widget(MaxCurrentScreen(name = 'maxcurrent'))
screen_manager.add_widget(OutletScreen(name = 'outlet'))
screen_manager.add_widget(GoodbyeScreen(name = 'goodbye'))


class DemoApp(MDApp):

    def build(self):
        print("main")
        self.theme_cls.primary_palette = "Green"
        self.screen = Builder.load_string(sc_helper) 
        
        return self.screen

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

    def save_tfvalue(self):
        usertext = self.root.ids.currentchargetf.text
        print(usertext)
    
        

if __name__ == '__main__':
    DemoApp().run()


