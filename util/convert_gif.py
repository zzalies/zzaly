import imageio
import urllib.request as ur
import io
from PIL import Image
import numpy
from util.get_root_path import get_root_path

class ConvGIF:
    def __init__(self):
        self.result = 0
        self.images = []

    def Convert(self,gifname, duration):
        root = get_root_path()
        imageio.mimsave(root + '/static/upload_image/'+gifname+'.gif',self.images,format='GIF',duration=duration)
        return root + '/static/upload_image/' + gifname + '.gif'

    def SetURL(self,url):
        file = io.BytesIO(ur.urlopen(url).read())
        img = numpy.asarray(Image.open(file))
        self.images.append(img)

    def SetFile(self,file):
        #img = numpy.asarray(Image.open(file))
        f = io.BytesIO(file)
        img = numpy.asarray(Image.open(f))
        self.images.append(img)
