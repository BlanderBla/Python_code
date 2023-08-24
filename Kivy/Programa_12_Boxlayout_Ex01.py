import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxlayoutApp(App):
    def build(self):
        main_superlayout = BoxLayout(
            orientation = 'vertical'
        )
        # 
        first_boxlayout = BoxLayout(
            orientation ='vertical',
            spacing = 5,
            padding = 30
        )
        bttn1 = Button(
            text='Button 1',
            font_size=20,
            background_color=(0.2,0.6,1,1)
        )
        bttn2 = Button(
            text='Button 1',
            font_size=20
        )
        first_boxlayout.add_widget(bttn1)
        first_boxlayout.add_widget(bttn2)

        # 
        second_boxlayout = BoxLayout(
            orientation = 'horizontal',
            spacing = 5,
            padding = 30
        )
        bttn3 = Button(
            text='Button 3',
            font_size = 20
        )
        bttn4 = Button(
            text='Button 4',
            font_size = 20
        )
        second_boxlayout.add_widget(bttn3)
        second_boxlayout.add_widget(bttn4)


        main_superlayout.add_widget(first_boxlayout)
        main_superlayout.add_widget(second_boxlayout)

        return main_superlayout

BoxlayoutApp().run()