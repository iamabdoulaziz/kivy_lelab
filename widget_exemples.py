from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_exemples.kv")

class WidgetsExemple(GridLayout):
    my_text = StringProperty("Hey !")
    conter = 0
    conter_actived = BooleanProperty(False)
    # slider_value_txt = StringProperty("Slider ")
    text_input_str = StringProperty("Cute boy")

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

    def on_switch_activate(self, widget):
        print(f"Switch: {str(widget.active)}")

    # def on_slider_value(self, widget):
        # print(f"Slider: {str(int(widget.value))}")
        # self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
