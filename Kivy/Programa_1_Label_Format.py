from kivy.app import App
from kivy.uix.label import Label

class KiviLabel(App):
    def build(self):
        return Label(text='[u][color=ff0066][b]Bienvenido[/b][/color] yo soy [i][color=ff9933]Brayan Adrian Galvan Flores[/i][/color][/u]', markup=True)
    
KiviLabel().run()