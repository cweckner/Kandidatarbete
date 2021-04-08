import kivy
kivy.require("1.11.1")

from kivy.config import Config
Config.set("kivy", "keyboard_mode", 'dock')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

class Calc(TextInput):
    def _keyboard_close(self):
        pass
    def setup_keyboard(self):
        kb = Window.request_keyboard(self._keyboard_close, self)
        if kb.widget:
            kb.widget.layout = 'numeric.json'

class TestApp(App):
    def build(self):
        root = Calc()
        root.setup_keyboard()
        return root

if __name__ == '__main__':
    TestApp().run()