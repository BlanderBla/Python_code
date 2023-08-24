from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class CustomBoxLayoutApp(App):
    def build(self):
        layout = BoxLayout(
            orientation='vertical',  # 'horizontal' para orientación horizontal
            spacing=10,  # Espacio entre widgets
            padding=20,  # Espacio de relleno alrededor del BoxLayout
            size_hint=(None, None),
            size=(400, 300))
        
        label1 = Label(text='Widget 1', font_size=20, color=(0.2, 0.6, 1, 1))
        label2 = Label(text='Widget 2', font_size=20, color=(0.8, 0.7, 8, 9),)
        label3 = Label(text='Widget 3', font_size=20, color=(0.2, 0.6, 1, 1))
        
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        
        return layout

if __name__ == '__main__':
    CustomBoxLayoutApp().run()
