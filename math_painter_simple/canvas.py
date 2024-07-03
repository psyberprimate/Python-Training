import numpy as np
from PIL import Image

class Canvas():
    
    def __init__(self, width : int, height : int, color : tuple):
        self.color = color
        self.width = width
        self.height = height
        self.pixel_data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.pixel_data[:] = self.color
        
    def make(self, image_path : str, image_name : str = "canvas"):
        img = Image.fromarray(self.pixel_data, 'RGB')
        img.save(image_path+image_name+'.png')
        
    