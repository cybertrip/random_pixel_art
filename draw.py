# Import Functions
#   > pillow (PIL) is for generating an image from an array
#   > numpy is for generating a three diemnsional array with color values of Lumninance, Chrominance Red and Chrominance Blue
#   > time is to give a delay to the program execution
from PIL import Image
import numpy as np
import time

# Draw Image from Array
#   > Generate an array that is a length by a width by 3
#   > Redraw is how many times you want the algorithm to draw the image
#   > Algorithm will save image as a jpeg
def drawImage(length, width, redraw):
  for x in range(0, redraw):
    array = np.random.randint(255, size = (length, width, 3), dtype=np.uint8)

    im = Image.fromarray(array).convert('YCbCr')
    im.save('random.jpeg')
    time.sleep(1/2)
