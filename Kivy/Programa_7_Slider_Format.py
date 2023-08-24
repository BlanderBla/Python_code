from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider

class SliderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Crear un Slider con atributos
        slider = Slider(
            min=0, max=100, value=50,
            orientation='horizontal',  # 'vertical' para orientación vertical
            step=1,  # Paso entre valores
            size_hint=(None, None),
            size=(300, 50),
            on_value_pos=self.on_slider_value_change)  # Función llamada al cambiar
        
        # Agregar el Slider al diseño
        layout.add_widget(Label(text='Valor: 50', font_size=18))
        layout.add_widget(slider)
        
        return layout
    
    def on_slider_value_change(self, instance, value):
        print(f"Valor del Slider: {value}")
    

SliderApp().run()

