from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

class SpinnerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Crear un Spinner con atributos
        spinner = Spinner(
            text='Selecciona una opción',
            values=['Opción 1', 'Opción 2', 'Opción 3'],
            size_hint=(None, None),
            size=(200, 50),
            on_text=self.on_spinner_select)  # Función llamada al seleccionar
        return spinner
    
    def on_spinner_select(self, instance, text):
        print(f"Opción seleccionada: {text}")

SpinnerApp().run()
