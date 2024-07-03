import app as MainApp
from kivy.lang import Builder

if __name__ == "__main__":
    
    Builder.load_file('photo_searcher/frontend.kv')
    MainApp.App().run()