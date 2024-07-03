from kivy.app import App
import screen_manager as ScreenManager
import screen as screen


class App(App):
    
    
    def build(self):
        return ScreenManager.RootWidget()
    
    