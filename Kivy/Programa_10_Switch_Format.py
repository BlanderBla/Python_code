from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch

class SwitchApp(App):
    def build(self):
        # Crear un Switch con atributos
        switch = Switch(
            active=False,
            size_hint=(None, None),
            size=(100, 50),
            on_active=self.on_switch_active)  # Función llamada al cambiar
        return switch
    def on_switch_active(self, instance, value):
        if value:
            print("Switch activado")
        else:
            print("Switch desactivado")

SwitchApp().run()
