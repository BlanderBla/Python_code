from kivy.app import App
from kivy.uix.checkbox import CheckBox

class CheckboxApp(App):
    def build(self):
        # Crear un Checkbox con atributos
        checkbox = CheckBox(
            active=False,
            color=(0.2, 0.6, 1, 1),
            size_hint=(None, None),
            size=(50, 50),
            on_active=self.on_checkbox_active)  # Función llamada al cambiar
        return checkbox
    
    def on_checkbox_active(self, instance, value):
        if value:
            print("Checkbox activado")
        else:
            print("Checkbox desactivado")

CheckboxApp().run()