from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class ToggleButtonApp(App):
    def build(self):
       # Crear un ToggleButton con atributos
        toggle_button = ToggleButton(
            text='Activo',
            font_size=20,
            background_color=(0.2, 0.6, 1, 1),
            background_normal='',
            background_down='button_pressed.png',  # Imagen para estado presionado
            group='group1',  # Grupo para manejar la selección mutua
            size_hint=(None, None),
            size=(200, 50),
            on_press=self.on_toggle_press)  # Función llamada al presionar
        return toggle_button
    
    def on_toggle_press(self, instance):
        if instance.state == 'normal':
            print("ToggleButton desactivado")
        else:
            print("ToggleButton activado")

ToggleButtonApp().run()
