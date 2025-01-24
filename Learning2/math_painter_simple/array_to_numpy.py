import numpy as np
from PIL import Image


#Create a 3d numpy array of zeros, then replace zeros (black pixels) with yellow pixels
data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255, 255, 0]

print(data)

#red patch
data[0:3, 0:2] = [255, 0, 0]
data[0:3, 2:4] = [255, 255, 200]
data[3:4, 2:4] = [0, 0, 0]


img = Image.fromarray(data, 'RGB')
img.save('math_painter/canvas.png')