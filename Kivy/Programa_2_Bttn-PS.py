from kivy.app import App
from kivy.uix.button import Button

class myButton(App):
    def build(self):
        return Button(text='Hola', pos=(300,350), size_hint=(.25,.18))

myButton().run()