

sc_helper = """

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
            text: "Open time picker"
            text_button_color: (1, 1, 1, .5)
            primary_color: (114, 34, 91)
            pos_hint: {'center_x': 0.6, 'center_y': 0.35}
            on_release: app.show_time_picker()  
        MDRaisedButton:
            id: datebutton
            text: "Open date picker"
            pos_hint: {'center_x': 0.4, 'center_y': 0.35}
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
            hint_text: "Enter the battery capacity"
            helper_text: ""
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300

    MaxCurrentScreen:
        id: maxcurrentscreen
        MDTextField:
            id: maxcurrenttf
            hint_text: "Enter max current of EV"
            helper_text: ""
            helper_text_mode: "on_focus"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
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
            pos_hint: {'center_x': 0.45, 'center_y': 0.4}
        MDCheckbox:
            id: checkbox2
            group: 'group'
            size_hint: None, None
            size: dp(48), dp(48)
            pos_hint: {'center_x': 0.6, 'center_y': 0.4}
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
    MDLabel:
        text: "Departure Date & Time"
        halign: 'center'
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
    ScrollView:
        MDList:
            id: carbrandlist
            OneLineAvatarListItem:
                text: 'Audi'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'audimodels'
                ImageLeftWidget:
                    source: "Images/audi_logo.png" 
            OneLineAvatarListItem:
                text: 'BMW'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'bmwmodels'
                ImageLeftWidget:
                    source: "Images/bmw_logo.png"
            OneLineAvatarListItem:
                text: 'Kia'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'kiamodels'
                ImageLeftWidget:
                    source: "Images/kia_logo.png"
            OneLineAvatarListItem:
                text: 'Mitsubishi'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'mitsubishimodels'
                ImageLeftWidget:
                    source: "Images/mitsubishi_logo.png"
            OneLineAvatarListItem:
                text: 'Nissan'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'nissanmodels'
                ImageLeftWidget:
                    source: "Images/nissan_logo.png"
            OneLineAvatarListItem:
                text: 'Renault'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'renaultmodels'
                ImageLeftWidget:
                    source: "Images/renault_logo.png"
            OneLineAvatarListItem:
                text: 'Volkswagen'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'volkswagenmodels'
                ImageLeftWidget:
                    source: "Images/volkswagen_logo.png"
            OneLineAvatarListItem:
                text: 'Volvo'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'volvomodels'
                ImageLeftWidget:
                    source: "Images/volvo_logo.png"
            OneLineAvatarListItem:
                text: 'Tesla'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'teslamodels'
                ImageLeftWidget:
                    source: "Images/tesla_logo.png"
            OneLineAvatarListItem:
                text: 'Other'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'batterycapacity'
                ImageLeftWidget:
                    source: "Images/other.png"
            
            
                
<AudiModelsScreen>:
    name: 'audimodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: 'E-TRON 50 Quattro'
                on_release: 
                    root.manager.transition.direction = 'left' 
                    root.manager.current = 'outlet'
                
            OneLineListItem:
                text: 'E-TRON 55 Quattro'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
               
            OneLineListItem:
                text: 'E-TRON Q4'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'                     
    MDLabel:
        text: 'Audi Models'
        halign: 'center'
<BmwModelsScreen>:
    name: 'bmwmodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: '330E Auto'
                on_release: 
                    root.manager.transition.direction = 'left' 
                    root.manager.current = 'outlet'
                
            OneLineListItem:
                text: '330E Xdrive'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
               
            OneLineListItem:
                text: 'I3 60 Ah'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet' 
            
            OneLineListItem:
                text: 'I3 120 Ah'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'I3s 120 Ah'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Bmw Models'
        halign: 'center'
        
<KiaModelsScreen>:
    name: 'kiamodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: 'OPTIMA'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
               
            OneLineListItem:
                text: 'NIRO'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet' 
            
            OneLineListItem:
                text: 'E-NIRO 42kWh'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'E-NIRO 67kWh'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Kia Models'
        halign: 'center'
        
<MitsubishiModelsScreen>:
    name: 'mitsubishimodels'
    ScrollView:
        MDList:
            id: carmodellist
            
            OneLineListItem:
                text: 'Outlander'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Mitsubishi Models'
        halign: 'center'
        
<NissanModelsScreen>:
    name: 'nissanmodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: 'LEAF'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'LEAF e+'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Nissan Models'
        halign: 'center'
        
<RenaultModelsScreen>:
    name: 'renaultmodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: 'KANGOO EXPRESS Z.E'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'ZOE GEN 2'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'ZOE '
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Renault Models'
        halign: 'center'
        
<VolkswagenModelsScreen>:
    name: 'volkswagenmodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: 'E-Golf'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'ID.3 - Pure'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                    
            OneLineListItem:
                text: 'ID.3 - Pro '
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                    
            OneLineListItem:
                text: 'ID.3 - PRO S'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'GOLF GTE'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                    
            OneLineListItem:
                text: 'Passat GTe '
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Volkswagen Models'
        halign: 'center'
        
<VolvoModelsScreen>:
    name: 'volvomodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: 'V90'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: 'V60 D6'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Volvo Models'
        halign: 'center'
        
<TeslaModelsScreen>:
    name: 'teslamodels'
    ScrollView:
        MDList:
            id: carmodellist
            OneLineListItem:
                text: 'S'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
                        
            OneLineListItem:
                text: '3'
                on_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'outlet'
    MDLabel:
        text: 'Tesla Models'
        halign: 'center'


<BatteryCapacityScreen>:
    name: 'batterycapacity'
    MDFlatButton:
        text: '4/6'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: 
            app.save_batterytf()
            root.manager.transition.direction = 'left'
            root.manager.current = 'maxcurrent'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'timedate'
    

<MaxCurrentScreen>:
    name: 'maxcurrent'
    MDFlatButton:
        text: '5/6'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: 
            app.save_maxcurrenttf()
            root.manager.transition.direction = 'left'
            root.manager.current = 'outlet'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'batterycapacity'

<OutletScreen>:
    name: 'outlet'
    MDLabel:
        text: 'Charging outlet'
        halign: 'center'
    MDFlatButton:
        text: '1'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.4, 'center_y': 0.4}
    MDFlatButton:
        text: '2'
        theme_text_color: "Hint"
        pos_hint: {'center_x': 0.55, 'center_y': 0.4}
    
    MDRectangleFlatButton:
        text: 'Charge'
        pos_hint: {'center_x': 0.9, 'center_y': 0.1}
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
            root.manager.current = 'maxcurrent'


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



