

sc_helper = """
#:import rgba kivy.utils.get_color_from_hex

ScreenManager:
    WelcomeScreen:
    InputScreen:
    CurrentChargeScreen:
        id: currentchargescreen
        MDTextField:
            id: currentchargetf
            hint_text: "Enter current charge level"
            helper_text: "Input should be in %"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300
    WantedChargeScreen:
        id: wantedchargescreen
        MDTextField:
            id: wantedchargetf
            hint_text: "Enter wanted charge level at departure"
            helper_text: "Input should be in %"
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300    
    TimeDateScreen:
        id: timedatescreen
        MDRaisedButton:
            id: timebutton
            text: app.timepicker
            md_bg_color: 1,1,1,1
            theme_text_color: "Custom"
            text_color: 0.46, 0.46, 0.46,1
            pos_hint: {'center_x': 0.5, 'center_y': 0.40}
            on_release: app.show_time_picker()  
        MDRaisedButton:
            id: datebutton
            text: app.datepicker
            md_bg_color: 1,1,1,1
            text_color: 0.46, 0.46, 0.46,1
            pos_hint: {'center_x': 0.5, 'center_y': 0.50}
            on_release: app.show_date_picker()  

    CarBrandScreen:
    AudiModelsScreen:
    BmwModelsScreen:
    KiaModelsScreen:
    MitsubishiModelsScreen:
    NissanModelsScreen:
    RenaultModelsScreen:
    VolkswagenModelsScreen:
    VolvoModelsScreen:
    TeslaModelsScreen:

    BatteryCapacityScreen:
        id: batterycapacityscreen
        MDTextField:
            id:  batterycapacitytf  
            hint_text: "Enter the battery capacity of EV"
            helper_text: ""
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            width: 300
        MDTextField:
            id: maxcurrenttf
            hint_text: "Enter max current of EV"
            helper_text: ""
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            size_hint_x: None
            width: 300

    OutletScreen:
        id: outletscreen
        MDCheckbox:
            id: checkbox1
            group: 'group'
            size_hint: None, None
            size: dp(48), dp(48)
            active: True
            pos_hint: {'center_x': 0.40, 'center_y': 0.4}
        MDCheckbox:
            id: checkbox2
            group: 'group'
            size_hint: None, None
            size: dp(48), dp(48)
            pos_hint: {'center_x': 0.65, 'center_y': 0.4}
    GoodbyeScreen:
        id: goodbyescreen


<WelcomeScreen>:
    name: 'welcome'
    on_enter:
        app.animate_the_label(welcomelabel)
    MDLabel:
        id: welcomelabel
        text: 'Welcome, please scan your RFID-tag'
        halign: 'center'

    MDIcon:
        id: wifiicon
        icon: "wifi"
        pos_hint: {'center_x': 0.98, 'center_y': 0.4}
        color: app.theme_cls.primary_color

    MDRectangleFlatButton:
        text: 'Go directly to inputs (For test purposes only)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'currentcharge'

<CurrentChargeScreen>:
    name: 'currentcharge'
    MDIconButton:
        id: infoicon
        icon: "information-outline"
        pos_hint: {'center_x': 0.90, 'center_y': 0.93}
        user_font_size: "20sp"
        theme_text_color: "Hint"
        on_release:
            app.show_info('currentcharge')
    MDFlatButton:
        text: '1/6'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press:
            app.save_currenttf() 
            root.manager.transition.direction = 'left'
            root.manager.current = 'wantedcharge'

            
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press:
            root.manager.transition.direction = 'right'            
            root.manager.current = 'welcome'
        

<WantedChargeScreen>:
    name: 'wantedcharge'
    MDIconButton:
        id: infoicon
        icon: "information-outline"
        pos_hint: {'center_x': 0.90, 'center_y': 0.93}
        user_font_size: "20sp"
        theme_text_color: "Hint"
        on_release:
            app.show_info('wantedcharge')
    MDFlatButton:
        text: '2/6'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: 
            app.save_wantedtf() 
            root.manager.transition.direction = 'left'
            root.manager.current = 'timedate'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'currentcharge'

<TimeDateScreen>:
    name: 'timedate'
    
    MDIconButton:
        id: infoicon
        icon: "information-outline"
        pos_hint: {'center_x': 0.90, 'center_y': 0.93}
        user_font_size: "20sp"
        theme_text_color: "Hint"
        on_release:
            app.show_info('timedate')
    
    BoxLayout:
        orientation: 'vertical'
        spacing: "50dp"
        padding: 0, 0, 0, "450dp"
        MDLabel:
            text: "Departure Date & Time"
            halign: 'center'
            font_style: "H6"
            adaptive_height: True
    
    MDIconButton:
        id: dateicon
        icon: "calendar"
        pos_hint: {"center_x": 0.35, "center_y": 0.50}
        #theme_text_color: "Custom"
        #text_color: app.theme_cls.primary_color
    
    MDIconButton:
        id: timeicon
        icon: "clock"
        pos_hint: {"center_x": 0.35, "center_y": 0.40}
        #theme_text_color: "Custom"
        #text_color: app.theme_cls.primary_color
            
    MDFlatButton:
        text: '3/6'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press:
            root.manager.transition.direction = 'left'         
            root.manager.current = 'carbrand'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'wantedcharge'

<CarBrandScreen>:
    name: 'carbrand'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Car brand"
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarbrand()]]
            right_action_items: [["information-outline", lambda x: app.show_info('carbrand')]]
                 
        ScrollView:
            MDList:
                id: carbrandlist
                OneLineAvatarListItem:
                    text: 'Audi'
                    on_release: 
                        app.set_previous_screen('audimodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'audimodels'
                    ImageLeftWidget:
                        source: "Images/audi_logo.png" 
                OneLineAvatarListItem:
                    text: 'BMW'
                    on_release:
                        app.set_previous_screen('bmwmodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'bmwmodels'
                    ImageLeftWidget:
                        source: "Images/bmw_logo.png"
                OneLineAvatarListItem:
                    text: 'Kia'
                    on_release: 
                        app.set_previous_screen('kiamodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'kiamodels'
                    ImageLeftWidget:
                        source: "Images/kia_logo.png"
                OneLineAvatarListItem:
                    text: 'Mitsubishi'
                    on_release:
                        app.set_previous_screen('mitsubishimodels') 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'mitsubishimodels'
                    ImageLeftWidget:
                        source: "Images/mitsubishi_logo.png"
                OneLineAvatarListItem:
                    text: 'Nissan'
                    on_release: 
                        app.set_previous_screen('nissanmodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'nissanmodels'
                    ImageLeftWidget:
                        source: "Images/nissan_logo.png"
                OneLineAvatarListItem:
                    text: 'Renault'
                    on_release: 
                        app.set_previous_screen('renaultmodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'renaultmodels'
                    ImageLeftWidget:
                        source: "Images/renault_logo.png"
                OneLineAvatarListItem:
                    text: 'Volkswagen'
                    on_release: 
                        app.set_previous_screen('volkswagenmodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'volkswagenmodels'
                    ImageLeftWidget:
                        source: "Images/volkswagen_logo.png"
                OneLineAvatarListItem:
                    text: 'Volvo'
                    on_release: 
                        app.set_previous_screen('volvomodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'volvomodels'
                    ImageLeftWidget:
                        source: "Images/volvo_logo.png"
                OneLineAvatarListItem:
                    text: 'Tesla'
                    on_release:
                        app.set_previous_screen('teslamodels')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'teslamodels'
                    ImageLeftWidget:
                        source: "Images/tesla_logo.png"
                OneLineAvatarListItem:
                    text: 'Other'
                    on_release: 
                        app.set_previous_screen('batterycapacity')
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'batterycapacity'
                    ImageLeftWidget:
                        source: "Images/other.png"
        
            
            
                
<AudiModelsScreen>:
    name: 'audimodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Audi Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'E-TRON 50 Quattro'
                    on_release: 
                        root.manager.transition.direction = 'left' 
                        root.manager.current = 'outlet'
                        app.CARSPEC('AUDI', 'E-TRON 50 Quattro')
                    
                OneLineListItem:
                    text: 'E-TRON 55 Quattro'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('AUDI', 'E-TRON 55 Quattro')
                
                OneLineListItem:
                    text: 'E-TRON Q4'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('AUDI', 'E-TRON Q4')   
                      
    
<BmwModelsScreen>:
    name: 'bmwmodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "BMW Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: '330E Auto'
                    on_release: 
                        root.manager.transition.direction = 'left' 
                        root.manager.current = 'outlet'
                        app.CARSPEC('BMW', '330E Auto')
                    
                OneLineListItem:
                    text: '330E Xdrive'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('BMW', '330E Xdrive')
                
                OneLineListItem:
                    text: 'I3 60 Ah'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet' 
                        app.CARSPEC('BMW', 'I3 60 Ah')
                
                OneLineListItem:
                    text: 'I3 120 Ah'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('BMW', 'I3 120 Ah')
                            
                OneLineListItem:
                    text: 'I3s 120 Ah'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('BMW', 'I3s 120 Ah')
          
   
        
<KiaModelsScreen>:
    name: 'kiamodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Kia Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'OPTIMA'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('KIA', 'OPTIMA')
                
                OneLineListItem:
                    text: 'NIRO'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('KIA', 'NIRO') 
                        
                
                OneLineListItem:
                    text: 'E-NIRO 42kWh'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('KIA', 'E-NIRO 42kWh')
                            
                OneLineListItem:
                    text: 'E-NIRO 67kWh'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('KIA', 'E-NIRO 67kWh')  
  
        
<MitsubishiModelsScreen>:
    name: 'mitsubishimodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Mitsubishi Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'OUTLANDER'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('MITUBISHI', 'OUTLANDER')
         
 
        
<NissanModelsScreen>:
    name: 'nissanmodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Nissan Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'LEAF'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('NISSAN', 'LEAF')
                            
                OneLineListItem:
                    text: 'LEAF e+'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('NISSAN', 'LEAF e+')
   
        
<RenaultModelsScreen>:
    name: 'renaultmodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Renault Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'KANGOO EXPRESS Z.E'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('RENAULT', 'KANGOO EXPRESS Z.E')
                            
                OneLineListItem:
                    text: 'ZOE GEN 2'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('RENAULT', 'ZOE GEN 2')
                            
                OneLineListItem:
                    text: 'ZOE '
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('RENAULT', 'ZOE')  
   
        
<VolkswagenModelsScreen>:
    name: 'volkswagenmodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Volkswagen Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'E-Golf'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volkswagen', 'E-Golf')
                            
                OneLineListItem:
                    text: 'ID.3 - Pure'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volkswagen', 'ID.3 - Pure')
                        
                OneLineListItem:
                    text: 'ID.3 - Pro '
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volkswagen', 'ID.3 - PRO S')
                        
                        
                OneLineListItem:
                    text: 'ID.3 - PRO S'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volkswagen', 'ID.3 - PRO S')
                            
                OneLineListItem:
                    text: 'GOLF GTE'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volkswagen', 'GOLF GTE')
                        
                OneLineListItem:
                    text: 'Passat GTe'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volkswagen', 'Passat GTe')
   
        
<VolvoModelsScreen>:
    name: 'volvomodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Volvo Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'V90'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volvo', 'V90')
                            
                OneLineListItem:
                    text: 'V60 D6'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Volvo', 'V60 D6') 
   
        
<TeslaModelsScreen>:
    name: 'teslamodels'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Tesla Models"
            md_bg_color: app.theme_cls.accent_color
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: root.callbackcarmodel()]]
        ScrollView:
            MDList:
                id: carmodellist
                OneLineListItem:
                    text: 'S'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Tesla', 'S')
                            
                OneLineListItem:
                    text: '3'
                    on_release: 
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'outlet'
                        app.CARSPEC('Tesla', '3')
   

<BatteryCapacityScreen>:
    name: 'batterycapacity'

    MDIconButton:
        id: infoiconbatterycapacity
        icon: "information-outline"
        pos_hint: {'center_x': 0.90, 'center_y': 0.93}
        user_font_size: "20sp"
        theme_text_color: "Hint"
        on_release:
            app.show_info('batterycapacity')

        
    MDFlatButton:
        text: '5/6'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: 
            app.save_batterytf()
            app.save_maxcurrenttf()
            root.manager.transition.direction = 'left'
            root.manager.current = 'outlet'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'carbrand'
    

<OutletScreen>:
    name: 'outlet'
    MDIconButton:
        id: infoiconbatterycapacity
        icon: "information-outline"
        pos_hint: {'center_x': 0.90, 'center_y': 0.93}
        user_font_size: "20sp"
        theme_text_color: "Hint"
        on_release:
            app.show_info('outlet')
    MDLabel:
        text: 'Charging outlet'
        halign: 'center'
    MDFlatButton:
        text: '1'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.35, 'center_y': 0.4}
    MDFlatButton:
        text: '2'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.60, 'center_y': 0.4}
    
    MDRectangleFlatButton:
        text: 'Charge'
        pos_hint: {'center_x': 0.8, 'center_y': 0.1}
        on_press:
            app.save_outletcbx()
            app.print_tfvalues()
            root.manager.current = 'goodbye'
    MDFlatButton:
        text: '6/6'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton: 
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = app.get_previous_screen()


<GoodbyeScreen>:
    name: 'goodbye'
    on_enter:
        app.animate_the_label(goodbyelabel)
    MDLabel:
        id: goodbyelabel
        text: 'Thank you, your car will now charge optimally'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Go back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'outlet'
    
"""



