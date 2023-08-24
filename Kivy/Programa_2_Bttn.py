from kivy.app import App
from kivy.uix.button import Button
from functools import partial

# Botón normal
class myButton(App):
    def build(self):
        return Button(text='Entrar', background_color=(0.61, 0, 0.20, 0.53)) 
myButton().run()
