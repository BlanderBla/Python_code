import kivy
import random as rnd

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,0,1,1]
blue = [0,0,1,1]
purple = [1,0,1,1,]

class Layout(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(
                text="Button #%s" %(i+1)
            )
            layout.add_widget(btn)
        return layout

Layout().run()