from kivy.lang import Builder
import photo_share_app as photo

if __name__ == "__main__":
    Builder.load_file('camera_photo_sharer/frontend.kv')
    photo.PhotoApp().run()