from kivy.app import App
from kivy.uix.button import Button
from functools import partial

class myButton(App):
    def disable(self, instance, *args):
        instance.disabled = True
    
    def update(self, instance, *args):
        instance.text = "Disable"
    
    def build(self):
        bttn = Button(text='Click for disable')
        bttn.bind(on_press=partial(self.disable, bttn))
        bttn.bind(on_press=partial(self.update, bttn))
        return bttn
    
myButton().run()
