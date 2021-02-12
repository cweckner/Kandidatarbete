

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
    MDLabel:
        text: 'Welcome, please scan your RFID-tag'
        halign: 'center'

    MDIcon:
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
            root.manager.current = 'batterycapacity'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'wantedcharge'

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
    MDLabel:
        text: 'Thank you, your car will now charge optimally'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Go back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: 
            root.manager.transition.direction = 'right'
            root.manager.current = 'outlet'
    
"""



