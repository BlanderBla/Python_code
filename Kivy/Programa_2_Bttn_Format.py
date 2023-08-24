from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        
        # Crear un botón con atributos
        button = Button(
            text='Haz clic',
            font_size=20,
            background_color=(0.2, 0.6, 1, 1),
            background_normal='',
            background_down='button_pressed.png',  # Imagen para estado presionado
            size_hint=(None, None),
            size=(200, 50),
            on_press=self.on_button_press)  # Función llamada al presionar
        return button

ButtonApp().run()