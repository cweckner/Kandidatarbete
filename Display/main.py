import csv
from kivymd.app import MDApp
from screen_nav import sc_helper
from datetime import date
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from kivymd.uix.list import OneLineAvatarListItem, OneLineListItem, MDList, ImageLeftWidget, ContainerSupport
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard 
from kivy.config import Config
from time import sleep
import datetime
import sys
import os
sys.path.insert(1, '/home/nora/School/Kandidatarbete/Microcontroller')
import backend
import commands
import threading


#from Microcontroller import optireal
Window.size = (480, 800) #WxH
Config.set('kivy', 'keyboard_layout', 'numeric.json')
print(Config.get('kivy', 'keyboard_layout'))
Config.set("kivy", "keyboard_mode", 'dock')

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

class CarBrandScreen(Screen):
    def callbackcarbrand(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'timedate'
        

class AudiModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

    

class BmwModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class KiaModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class MitsubishiModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class NissanModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class RenaultModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class VolkswagenModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class VolvoModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class TeslaModelsScreen(Screen):
    def callbackcarmodel(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'carbrand'

class BatteryCapacityScreen(Screen):
    pass

class OutletScreen(Screen):
    pass

class SummaryScreen(Screen):
    pass

class GoodbyeScreen(Screen):
    pass



screen_manager = ScreenManager()
screen_manager.add_widget(WelcomeScreen(name = 'welcome'))
screen_manager.add_widget(InputScreen(name = 'inputs'))
screen_manager.add_widget(CurrentChargeScreen(name = 'currentcharge'))
screen_manager.add_widget(WantedChargeScreen(name = 'wantedcharge'))
screen_manager.add_widget(TimeDateScreen(name = 'timedate'))
screen_manager.add_widget(CarBrandScreen(name = 'carbrand'))
screen_manager.add_widget(AudiModelsScreen(name = 'audimodels'))
screen_manager.add_widget(BmwModelsScreen(name = 'bmwmodels'))
screen_manager.add_widget(KiaModelsScreen(name = 'kiamodels'))
screen_manager.add_widget(MitsubishiModelsScreen(name = 'mitsubishimodels'))
screen_manager.add_widget(NissanModelsScreen(name = 'nissanmodels'))
screen_manager.add_widget(RenaultModelsScreen(name = 'renaultmodels'))
screen_manager.add_widget(VolkswagenModelsScreen(name = 'volkswagenmodels'))
screen_manager.add_widget(VolvoModelsScreen(name = 'volvomodels'))
screen_manager.add_widget(TeslaModelsScreen(name = 'teslamodels'))
screen_manager.add_widget(BatteryCapacityScreen(name = 'batterycapacity'))
screen_manager.add_widget(OutletScreen(name = 'outlet'))
screen_manager.add_widget(SummaryScreen(name = 'summary'))
screen_manager.add_widget(GoodbyeScreen(name = 'goodbye'))




class DemoApp(MDApp):
    showondatepicker="Choose date"
    showontimepicker= "Choose time"
    datepicker = ""
    timepicker = ""
    readytosend= False
    previousscreen= ""
    global dialog
    tfvalues = {'timepicker': '20.00'}
    global brand
    global model
    transactionID = "00000000-0000-0000-0000-000000000000"
    anim_or_not = 0

    global charger_taken; # set [True, True],[True, False], [False, True], [False, False] i konstruktorn
    #konstruktor
    

#    def __init__(self, one, two):
#        charger_taken = [one, two]


    def build(self):
        print("main")
        self.theme_cls.primary_palette = "Green"
        self.screen = Builder.load_string(sc_helper) 
        return self.screen
        
        

    def CARSPEC(self,b,m):
        with open(r'Bilkap.csv','r') as infile:
            reader = csv.reader(infile, delimiter=",")
            for row in reader:
                if b == row[0]:
                    if m == row[1]:
                        global batterytf
                        batterytf = row[2]
                        global maxcurrenttf 
                        maxcurrenttf = row[3]
                        print(batterytf)
                        print(maxcurrenttf)
                        self.brand = b
                        self.model = m

    
    def animate_the_label(self, widget, time):
        print(self.anim_or_not)
        if self.anim_or_not != 3:
            anim = Animation(opacity=0.1, duration=time) + Animation(opacity=1, duration=time)
            anim.bind(on_complete=self.callback_animation)
            anim.repeat = True
            anim.start(widget)  
            print(widget)
            self.anim_or_not += 1


    def stop_animating(self, widget):
        anim.cancel(widget)
    
    def callback_animation(self, *args):
        print("I'm done!")
  
    
    def set_previous_screen(self, widget):
        self.previousscreen = widget

    def get_previous_screen(self):
        return self.previousscreen

    def show_info(self, widget):
        self.dialog = MDDialog(
        title=self.info_title(widget),
        text=self.info_text(widget),
        buttons=[
            MDFlatButton(
                text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
            )])
        self.dialog.open()
    
    def info_title(self, widget):
        return {
            'currentcharge': "Current charge level",
            'wantedcharge': "Wanted charge level",
            'batterycapacity': "Battery capacity & maximum current",
            'timedate': "Time & Date of departure",
            'carbrand': "Car brand",
            'outlet': "Outlet"

        }.get(widget)
    
    def info_text(self, widget):
        return {
            'currentcharge': "Current charge level of your car's battery. Huur vet man?",
            'wantedcharge': "Desired charge level of your car's battery at the time of your next departure",
            'batterycapacity': "Your car model is not in our systems, please enter your car's battery capacity and maximum current manually. If you don't know these specifications, check the car brand's website or contact your car provider directly.",
            'timedate': "Date and time of the next departure of your car. The date and time are approximate values, but try to be specific to get the best results. If the car is used before the time chosen here there is a risk of it not being charged fully to the desired charge level.\n\nThere is a limit of 1 week ahead of today's date because the algorithm won't gain anything past that. ",
            'carbrand': "Please select the car's brand and model. If your car is not in the list we unfortunately do not have it in our systems, select the option  'Other' and manually enter the car's battery capacity and battery's maximum current.",
            'outlet': "The outlet in which your car is plugged in on the charging station. "

        }.get(widget)

    def close_dialog(self, widget):
        self.dialog.dismiss(force=True)

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        self.timepicker = str(time)
        self.showontimepicker = self.timepicker[:5]
        self.root.ids.timebutton.text = self.showontimepicker

    def on_save(self, instance, value, date_range):
        self.datepicker = str(value)
        self.showondatepicker = str(value)
        self.root.ids.datebutton.text = self.showondatepicker
        
    def show_date_picker(self):
        today = date.today()
        end_date = today + datetime.timedelta(days=7)        
        date_dialog = MDDatePicker(
            min_date=datetime.date(date.today().year, date.today().month, date.today().day), 
            max_date=datetime.date(end_date.year, end_date.month, end_date.day), 
            primary_color=get_color_from_hex("#70C170"), 
            text_toolbar_color=get_color_from_hex("#244511"), 
            selector_color=get_color_from_hex("#70C170"))
        
        date_dialog.bind(on_save=self.on_save)
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
        self.tfvalues = {
            'currenttf': currenttf,
            'wantedtf': wantedtf,
            'batterytf': batterytf,
            'maxcurrenttf': maxcurrenttf,
            'outletcbx': outletcbx,
            'timepicker': self.timepicker,
            'datepicker': self.datepicker
        }
        global date_timestr
        date_timestr = str(self.datepicker)+ " " +str(self.timepicker)
    
    def ready_to_send(self):
        self.readytosend = True
        print(self.tfvalues)

    def return_tfvalues(self):
        if self.datepicker == "" or self.timepicker == "":
            at = ""
        else:
            at = " at "
        self.root.ids.currentsummary.text = self.tfvalues['currenttf']
        self.root.ids.wantedsummary.text = self.tfvalues['wantedtf']
        self.root.ids.datetimesummary.text = self.tfvalues['datepicker'] + at + (self.tfvalues['timepicker'])[:5]
        self.root.ids.outletsummary.text = self.tfvalues['outletcbx']
        if self.brand != '':
            self.root.ids.brandorbatterysummary.text = 'Brand'
            self.root.ids.modelormaxcurrentsummary.text = 'Model'

            self.root.ids.brandorbatteryvaluesummary.text = self.brand
            self.root.ids.modelormaxcurrentvaluesummary.text = self.model
        else:
            self.root.ids.brandorbatterysummary.text = 'Battery capacity'
            self.root.ids.modelormaxcurrentsummary.text = 'Maximum current'

            self.root.ids.brandorbatteryvaluesummary.text = self.tfvalues['batterytf']
            self.root.ids.modelormaxcurrentvaluesummary.text = self.tfvalues['maxcurrenttf']

    def reset_brand_model(self):
        self.brand = ''
        self.model = ''
    
    def disable_charger(self, charger):
        charger_taken = [False, False]
        return charger_taken[charger-1]
    
    def charge_or_dialog(self, root):
        if currenttf != "" and wantedtf != "" and batterytf != "" and maxcurrenttf != "" and self.timepicker != "Choose time" and self.datepicker != "Choose date":
            self.ready_to_send()
            #download_thread = threading.Thread(target=self.return_values_to_backend(), name="Backend")
            #download_thread.start()
            self.return_values_to_backend()
            root.manager.current = 'goodbye'
           
        else:
            self.dialog = MDDialog(
            title= "Oops..!",
            text="Please, fill out all parameters before you charge",
            buttons=[
                MDFlatButton(
                text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
            )])
            self.dialog.open()


    def set_focus(self, textfield):
        if (textfield == 'currentcharge'):
            self.root.ids.currentchargetf.focus = True 
        if (textfield == 'wantedcharge'):
            self.root.ids.wantedchargetf.focus = True
        if (textfield == 'batterycapacity'):
            self.root.ids.batterycapacitytf.focus = True
        if (textfield == 'maxcurrent'):
            self.root.ids.maxcurrenttf.focus = True
   
    def restart(self):
        self.tfvalues.clear()
        self.reset_brand_model()
        currenttf = ""
        self.root.ids.wantedchargetf.text = ""
        wantedtf = ""
        self.root.ids.batterycapacitytf.text = ""
        batterycapacitytf = ""
        self.root.ids.currentchargetf.text = ""
        maxcurrenttf = ""
        self.root.ids.maxcurrenttf.text = ""
        self.timepicker = ""
        self.root.ids.timebutton.text = "Choose time"
        self.datepicker = ""
        self.root.ids.datebutton.text = "Choose date"
        self.readytosend = False


    #OBS hårdkodat in import backend för egen dator!!
    def return_values_to_backend(self):
        backendTest = backend.backend()
        transactionID = commands.incrementTransactionID(transactionID)
        backendTest.chargingLoop( True, int(self.tfvalues['currenttf']), int(self.tfvalues['wantedtf']), int(self.tfvalues['batterytf']), int(self.tfvalues['maxcurrenttf']), date_timestr, int(self.tfvalues['outletcbx']), currentTransactionID)

if __name__ == '__main__':
    DemoApp().run()




