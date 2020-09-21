# Pull Function from app.py and draw.py
from app import start, drawImage
from draw import *
from gui import *
from gui_support import *


# Start app
vp_start_gui()
print(gui_support.generateButton.get())

# Create Image
length = int(gui_support.lengthInput.get())
width = int(gui_support.widthInput.get())

drawImage(width, length, 1)

start()