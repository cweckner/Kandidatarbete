

sc_helper = """

ScreenManager:
    WelcomeScreen:
    LoginScreen:
    InputScreen:


<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'Welcome, please scan your RFID-tag'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'or log in manually'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'login'


<LoginScreen>:
    name: 'login'
    MDTextField:
        hint_text: "Enter username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        

<InputScreen>:
    name: 'inputs'
    
"""



