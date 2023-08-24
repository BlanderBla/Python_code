from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar

class ProgressBarApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Crear un ProgressBar con atributos
        progress_bar = ProgressBar(
            value=50,
            max=100,
            size_hint=(None, None),
            size=(300, 20))
        
        # Agregar el ProgressBar al diseño
        layout.add_widget(Label(text='Progreso: 50%', font_size=18))
        layout.add_widget(progress_bar)
        return layout
ProgressBarApp().run()
