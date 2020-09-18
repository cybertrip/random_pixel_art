# Import Pillow and tkinter
#   > tkinker is graphics module
#   > pillow is the image conversion modules
from PIL import ImageTk, Image
import tkinter

# Pull Function from draw.py
from draw import drawImage

# Construct App To Display Image
#   > Image is called random.jpeg as stated in draw.py
#   > Fills the whole window
def start():
  root = tkinter.Tk()
  
  root.title("Image Generator")

  # Size of image itself (512 x 512)
  root.geometry("512x512")
  
  img = ImageTk.PhotoImage(Image.open("random.jpeg")) 
  panel = tkinter.Label(root, image = img) 
  panel.pack(side = "bottom", fill = "both", expand = "yes") 
  
  root.mainloop()