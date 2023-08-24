from kivy.app import App
from kivy.uix.label import Label

class Saludo(App):
    def build(self):
        return Label(text = "Hola mundo")
    

Saludo().run()
