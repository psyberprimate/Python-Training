from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from filesharer import FileSharer
import time

class CameraScreen(Screen):
    """
    Class for controlling the camera screen
    
    Args:
        Screen (_type_): inherited from kivy.uix.screenmanager
    """    
    def start(self):
        """
        Camera start and button text change
        """        
        self.ids.camera_id.play = True
        self.ids.camera_control.text = "Close Camera"
        self.ids.camera.texture = self.ids.camera_id._camera.texture
    
    def close(self):
        """
        Camera stop and button text change
        """        
        self.ids.camera_id.play = False
        self.ids.camera_control.text = "Start Camera"
        self.ids.camera.texture = None
    
    def capture(self):
        """
        Create a filename with current time while capturing current frame as a photo and saving a photo image
        """        
        current_file_time = time.strftime('%Y%m%d-%H%M%S')
        file_path = '/photo_share_app/pictures/'
        self.file_full_path = file_path + current_file_time + '.png'
        self.ids.camera.export_to_png(self.file_full_path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img_id.source = self.file_full_path


class ImageScreen(Screen):
    
    def create_link(self):
        """
        Access the photo provided in the filepath and upload the phto to the web and show the web link in label widget
        """        
        file_path = PhotoApp.get_running_app().root.ids.camera_screen.self.manager.file_full_path
        # remember to provide API key for 'api_key' attribute
        file_sharing = FileSharer(filepath=file_path, api_key='') # init fileshare class with path
        self.ids.text_id.text = file_sharing.share() # URL

class RootWidget(ScreenManager):
    pass


class PhotoApp(App):
    
    def build(self):
        return RootWidget()