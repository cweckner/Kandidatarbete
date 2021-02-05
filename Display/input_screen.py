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
