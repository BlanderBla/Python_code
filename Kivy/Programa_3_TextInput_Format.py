from kivy.app import App
from kivy.uix.textinput import TextInput

class TextInputApp(App):
    # Crear un TextInput con atributos
    def build(self):
        text_input = TextInput(
            text='Texto de ejemplo',
            font_size=20,
            foreground_color=(0.2, 0.6, 1, 1),
            background_color=(0.9, 0.9, 0.9, 1),
            multiline=True,
            readonly=False,
            password=False,
            size_hint=(None, None),
            size=(200, 50))
        return text_input

TextInputApp().run()