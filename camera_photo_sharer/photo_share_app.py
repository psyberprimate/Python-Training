from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from filesharer import FileSharer
from kivy.core.clipboard import Clipboard
import time
import webbrowser

class CameraScreen(Screen):
    """Class for controlling the camera screen
    """    
    def start(self):
        """Camera start and button text change
        """        
        self.ids.camera_id.opacity = 1
        self.ids.camera_id.play = True
        self.ids.camera_control.text = "Close Camera"
        self.ids.camera.texture = self.ids.camera_id._camera.texture
    
    def close(self):
        """Camera stop and button text change
        """        
        self.ids.camera_id.opacity = 0
        self.ids.camera_id.play = False
        self.ids.camera_control.text = "Start Camera"
        self.ids.camera.texture = None
    
    def capture(self):
        """Create a filename with current time while capturing current frame as a photo and saving a photo image
        """        
        current_file_time = time.strftime('%Y%m%d-%H%M%S')
        file_path = '/photo_share_app/pictures/'
        self.file_full_path = file_path + current_file_time + '.png'
        self.ids.camera.export_to_png(self.file_full_path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img_id.source = self.file_full_path


class ImageScreen(Screen):
    
    """Class for screen for showing the picture and options
    """    
    link_error_message = 'Create a photo link first'
    
    def create_link(self):
        """Access the photo provided in the filepath and upload the phto to the web and show the web link in label widget
        """        
        file_path = PhotoApp.get_running_app().root.ids.camera_screen.self.manager.file_full_path
        # remember to provide API key for 'api_key' attribute
        file_sharing = FileSharer(filepath=file_path, api_key='') # init fileshare class with path
        self.url_address = file_sharing.share() # URL
        self.ids.text_id.text = self.url_address

    def copy_link(self):
        try:
            Clipboard.copy(self.url_address)
        except Exception as e:
            self.ids.text_id.text = self.link_error_message
            print(e)
            
    def open_link(self):
        try:
            webbrowser.open(self.url_address)
        except Exception as e:
            print(e)
            self.ids.text_id.text = self.link_error_message
            
class RootWidget(ScreenManager):
    pass


class PhotoApp(App):
    
    def build(self):
        return RootWidget()