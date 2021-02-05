

sc_helper = """

ScreenManager:
    WelcomeScreen:
    InputScreen:
    CurrentChargeScreen:
    WantedChargeScreen:
    TimeDateScreen:
    BatteryCapacityScreen:
    MaxCurrentScreen:
    OutletScreen:
    GoodbyeScreen:


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
        text: 'Go directly to input screen (For test purposes only)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'inputs'


<InputScreen>:
    name: 'inputs'

    Label: 
        text: "Kivy label"
        font_size: "30sp"
        pos_hint: {"center_x": .5, "center_y": .5}


    MDLabel:
        text_size: self.size
        text: 'Insert User Input'
        pos_hint: {"center_x": .5, "center_y": .5}

    MDTextField:
        hint_text: "Current battery level %"
        mode: "rectangle"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.75}

    MDTextField:
        hint_text: "Wanted charge level at departure %"
        mode: "rectangle"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.65}

    MDTextField:
        hint_text: "Battery Capacity"
        mode: "rectangle"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.55}

    MDTextField:
        hint_text: "Max current of EV battery"
        mode: "rectangle"
        size_hint_x: 0.5
        pos_hint: {'center_x': 0.3, 'center_y': 0.45}

    MDLabel:
        text: "Departure Date & Time"
        pos_hint: {'center_x': 0.6, 'center_y': 0.35}

    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': 0.4, 'center_y': 0.35}
        on_release: app.show_time_picker()

    MDRaisedButton:
        text: "Open date picker"
        pos_hint: {'center_x': 0.6, 'center_y': 0.35}
        on_release: app.show_date_picker()

    MDRectangleFlatButton:
        text: 'Go alternative route'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'currentcharge'


<CurrentChargeScreen>:
    name: 'currentcharge'
    MDTextField:
        hint_text: "Enter current charge level"
        helper_text: "Input should be in %"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: root.manager.current = 'wantedcharge'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: root.manager.current = 'inputs'

<WantedChargeScreen>:
    name: 'wantedcharge'
    MDTextField:
        hint_text: "Enter wanted charge level at departure"
        helper_text: "Input should be in %"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDFlatButton:
        text: '2/6'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: root.manager.current = 'timedate'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: root.manager.current = 'currentcharge'

<TimeDateScreen>:
    name: 'timedate'

    MDLabel:
        text: "Departure Date & Time"
        halign: 'center'

    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': 0.6, 'center_y': 0.35}
        on_release: app.show_time_picker()

    MDRaisedButton:
        text: "Open date picker"
        pos_hint: {'center_x': 0.4, 'center_y': 0.35}
        on_release: app.show_date_picker()
    MDFlatButton:
        text: '3/6'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: root.manager.current = 'batterycapacity'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: root.manager.current = 'wantedcharge'

<BatteryCapacityScreen>:
    name: 'batterycapacity'
    MDTextField:
        hint_text: "Enter the battery capacity"
        helper_text: ""
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDFlatButton:
        text: '4/6'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: root.manager.current = 'maxcurrent'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: root.manager.current = 'timedate'
    

<MaxCurrentScreen>:
    name: 'maxcurrent'
    MDTextField:
        hint_text: "Enter max current of EV"
        helper_text: ""
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDFlatButton:
        text: '5/6'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        on_press: root.manager.current = 'outlet'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: root.manager.current = 'batterycapacity'

<OutletScreen>:
    name: 'outlet'
    MDRectangleFlatButton:
        text: 'Charge'
        pos_hint: {'center_x': 0.9, 'center_y': 0.1}
        on_press: root.manager.current = 'goodbye'
    MDFlatButton:
        text: '6/6'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x": 0.1, "center_y": 0.1}
        on_press: root.manager.current = 'maxcurrent'


<GoodbyeScreen>:
    name: 'goodbye'
    MDLabel:
        text: 'Thank you, your car will now charge optimally'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Go back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'inputs'
    
"""



