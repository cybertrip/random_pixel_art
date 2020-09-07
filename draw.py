import numpy as np
from PIL import Image

def drawImage(length, width):
  array = np.random.randint(255, size = (length, width, 3), dtype=np.uint8)
  print(array)

  im = Image.fromarray(array).convert('YCbCr')
  im.save('random.jpeg')