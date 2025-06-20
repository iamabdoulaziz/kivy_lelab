

from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class WidgetsExemple(GridLayout):
    my_text = StringProperty("Hey !")
    conter = 0
    conter_actived = BooleanProperty(False)

    def on_button_click(self):
        print("Button click")
        # self.my_text = "Hello"
        if self.conter_actived is True:
            self.conter = self.conter + 1
            self.my_text = str(self.conter)


    def on_toggle_button_state(self, widget):
        print(f'toggle state {widget.state}')
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.conter_actived = False
        else:
            print("ON")
            widget.text = "ON"
            self.conter_actived = True



class MainWidget(Widget):
    pass

class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)) )
            self.add_widget(b)

#class GridLayoutExemple(GridLayout):
#    pass

class AnchorLayoutExemple(AnchorLayout):
    pass

class BoxLayoutExemple(BoxLayout):
    pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text= "A")
        self.add_widget(b1)
        b2 = Button(text="B")
        self.add_widget(b2)
        """

class LeLabApp(App):
    pass

LeLabApp().run()
