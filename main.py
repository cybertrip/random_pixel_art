from draw import drawImage
from flexx import flx

drawImage(512, 512, 1)

class Example(flx.Widget):
  def init(self):
    with flx.VBox():
      flx.Button(text='hello', flex=1)
      flx.Button(text='world', flex=2)

flx.launch(Example)
flx.run()