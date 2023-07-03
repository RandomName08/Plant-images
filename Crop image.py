from matplotlib import image
from matplotlib import pyplot
import numpy
from PIL import Image

im = numpy.array(Image.open('E:\Maybe\8a2c974a-8683-4936-9752-348b4142d418.jpg'))

print("Before trimming:",im.shape)
height = im.shape[0]
width = im.shape[1]
snheight = height/2
int(snheight)
snwidth = width/2
int(snwidth)
im_trim = im[snheight, snwidth]
print("After trimming:",im_trim.shape)
pyplot.imshow(im_trim)
pyplot.show()