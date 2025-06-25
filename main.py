from kivy.app import App
from kivy.properties import ObjectProperty
#from kivy.uix.gridlayout import GridLayout
# from kivy.uix.widget import Widget
from canvas_exemples import *
from navigation_screen_manager import NavigationScreenMangager


class MyScreenManager(NavigationScreenMangager):
    pass

class LeLabApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        # return CanvasExemple7()

LeLabApp().run()
