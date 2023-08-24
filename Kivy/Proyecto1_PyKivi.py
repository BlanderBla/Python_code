from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CalculadoraApp(App):
    def build(self):
        # Main BoxlaYout
        main_layout = BoxLayout(
            orientation = 'vertical'
        )
        # Label
        label_layout = BoxLayout(
            orientation = 'horizontal'
        )
        labelCal = Label(
            text = "Hola mundo",
            font_size = 20,
            color=(0.2, 0.6, 1, 1)
        )
        label_layout.add_widget(labelCal)
        lkey = keyboard()

        # Buttons
        button_layout = BoxLayout(
            orientation = 'horizontal'
        )
        for i in lkey:
            bttn = Button(
                text=i,
                font_size = 20
            )
            button_layout.add_widget(bttn)
        
        main_layout.add_widget(label_layout)
        main_layout.add_widget(button_layout)
        return main_layout

def keyboard():
    listKey = ['C','(',')','+','7','8','9','-','4','5','6','1','2','3','','/','0','.','=']
    return listKey

CalculadoraApp().run()