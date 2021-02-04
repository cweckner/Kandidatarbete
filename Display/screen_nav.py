

sc_helper = """

ScreenManager:
    WelcomeScreen:
    InputScreen:
    GoodbyeScreen:


<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'Welcome, please scan your RFID-tag'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Go directly to input screen (For test purposes only)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'inputs'


<InputScreen>:
    name: 'inputs'

    MDLabel:
        text: 'Insert User Input'
        halign: 'center'

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
        text: 'Go directly to goodbye screen'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'goodbye'


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



