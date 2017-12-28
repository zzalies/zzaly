import imageio
import urllib.request as ur
import io
from PIL import Image
import numpy

class ConvGIF:
    def __init__(self):
        self.result = 0
        self.images = []
    
    def Convert(self,gifname, duration):
        imageio.mimsave(gifname,self.images,format='GIF',duration=duration)

    def SetURL(self,url):
        file = io.BytesIO(ur.urlopen(url).read())
        img = numpy.asarray(Image.open(file))
        self.images.append(img)

    def SetFile(self,file):
        img = numpy.asarray(Image.open(file))
        self.images.append(img)
