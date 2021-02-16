from kivymd.app import MDApp
from screen_nav import sc_helper
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from kivy.utils import get_color_from_hex
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')




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
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        global timepicker
        timepicker = time
        print(time)

    def get_date(self, date):
        global datepicker
        datepicker = date
        print(date)

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def save_currenttf(self):
        global currenttf
        currenttf = self.root.ids.currentchargetf.text
        print(currenttf)

    def save_wantedtf(self):
        global wantedtf 
        wantedtf = self.root.ids.wantedchargetf.text
        print(wantedtf)

    def save_batterytf(self):
        global batterytf
        batterytf = self.root.ids.batterycapacitytf.text
        print(batterytf)

    def save_maxcurrenttf(self):
        global maxcurrenttf 
        maxcurrenttf = self.root.ids.maxcurrenttf.text
        print(maxcurrenttf)

    def save_outletcbx(self):
        global outletcbx 
        if self.root.ids.checkbox1.active:
            outletcbx = '1'
        else:
            outletcbx = '2'
        print(outletcbx)

    def print_tfvalues(self):
        global tfvalues
        tfvalues = {
            'currenttf': currenttf,
            'wantedtf': wantedtf,
            'batterytf': batterytf,
            'maxcurrenttf': maxcurrenttf,
            'outletcbx': outletcbx,
            'timepicker': timepicker,
            'datepicker': datepicker
        }
        print(tfvalues)
if __name__ == '__main__':
    DemoApp().run()