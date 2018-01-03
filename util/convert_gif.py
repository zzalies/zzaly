import imageio
import urllib.request as ur
import io
from PIL import Image
import numpy
#from util.get_root_path import get_root_path
from pytube import YouTube

class ConvGIF:
    def __init__(self):
        self.result = 0
        self.images = []
        self.vod_id = ""

    def Convert(self,gifname, duration):
        imageio.mimsave(get_root_path()+'/static/upload_image/'+gifname+'.gif',self.images,format='GIF',duration=duration)
        return '/static/upload_image/' + gifname + '.gif'

    def SetURL(self,url):
        file = io.BytesIO(ur.urlopen(url).read())
        img = numpy.asarray(Image.open(file).resize((250,250)))
        self.images.append(img)

    def SetFile(self,file):
        f = io.BytesIO(file)
        img = numpy.asarray(Image.open(f).resize((250,250)))
        self.images.append(img)

    def DownloadVideo(self,url):
        YouTube(url).get('mp4','720p').download('/static/tmp/')

    def DownloadAudio(self,url):
        pass

    def ConvertVideo(self,id):
        pass
