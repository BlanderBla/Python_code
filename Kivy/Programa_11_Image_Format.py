from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class ImageApp(App):
    def build(self):
        # Crear un widget Image con atributos
        image = Image(
            source='Jinx.jpg',  # Ruta de la imagen
            size_hint=(None, None),
            size=(200, 200),
            allow_stretch=True,  # Permitir estirar la imagen para ajustar el tamaño
            keep_ratio=True)     # Mantener la proporción original
        return image

ImageApp().run()
