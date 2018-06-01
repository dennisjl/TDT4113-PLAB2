from imager2 import *
from PIL import ImageOps
#modulen har metoder som:
#PIL.ImageOps.solarize(image, threshold=128) //threshold – All pixels above this greyscale level are inverted.
#PIL.ImageOps.posterize(image, bits)         //bits – The number of bits to keep for each channel (1-8)
#PIL.ImageOps.mirror(image)                  //rotates
#PIL.ImageOps.invert(image)                  //inverts
#PIL.ImageOps.grayscale(image)               //greyscales


class masterpiece():

    def __init__(self,im1,im2,im3):

        self.im1 = Imager(im1)
        self.im2 = Imager(im2)
        self.im3 = Imager(im3)


        self.im1 = self.im1.resize(220,220)
        self.im2 = self.im2.resize(220,220)
        self.im3 = self.im3.resize(220,220)

        self.create()

    def create(self):
        mix1=self.im3.morphroll(self.im1)         #kaller på morph4 metode i imager, ex morphroll tar inn steps som param as well
        mix2=self.im1.morphroll(self.im2)         #same
        self.masterpiece=blur(mix2).mortun(posterize(mix1),3)    #kaller  mortun, endrer accoriding til hvilken metode jeg vil bruke

    def exhibition(self):
        self.masterpiece.display()

def solarize(im):
    return Imager(image=ImageOps.solarize(im.image,128),width=im.xmax,height=im.ymax)   #bruker solarizemetoden i imageops

#PIL.ImageOps.posterize(image, bits)
def posterize(im):
    return Imager(image=ImageOps.posterize(im.image,8),width=im.xmax,height=im.ymax)

def blur(im):
    return Imager(image=im.image.filter(ImageFilter.GaussianBlur),width=im.xmax,height=im.ymax)

def main():
    mp = masterpiece('pinocchio', 'donaldduck',  'trump')
    mp.exhibition()

if __name__ == "__main__":
    main()

