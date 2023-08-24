from kivy.app import App
from kivy.uix.label import Label

class Label_App(App):
    def build(self): 
        # Crear una etiqueta con atributos
        label1 = Label(
            text='Etiqueta con atributos', 
            font_size=20, 
            color=(0.2, 0.6, 1, 1),  # Color en formato (R, G, B, A)
            italic=True, 
            bold=True, 
            underline=True,
            halign='center',  # Alineación horizontal: 'left', 'center', 'right'
            valign='middle',  # Alineación vertical: 'top', 'middle', 'bottom'
            size_hint=(None, None),  # Relativo al tamaño del padre
            size=(200, 50))  # Tamaño específico en píxeles
        return label1

Label_App().run()
