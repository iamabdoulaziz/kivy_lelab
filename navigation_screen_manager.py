from kivy.uix.screenmanager import ScreenManager


class NavigationScreenMangager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name


    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
        del self.screen_stack[-1]
        self.transition.direction = "right"

        self.current = screen_name