from matplotlib import image
from matplotlib import pyplot
import numpy
from PIL import Image

test = open('B&F1\gt.txt')
line = test.readline()
while line:
    print(line)
    data = line.split(',')
    imgid = data[0]
    letid = data[1]
    xcor = data[2]
    ycor = data[3]
    width = data[4]
    height = data[5]
    im = image.imread("B&F1\img\otest.png")
    xuse = int(xcor)
    yuse = im.shape[0] - int(ycor)
    widuse = xuse + int(width)
    heuse = yuse + int(height)
    print(imgid, letid, xcor, ycor, width, height)
    print(xuse, heuse)
    print(widuse, yuse)
    cropped = im[yuse:heuse, xuse:widuse]
    pyplot.imshow(cropped)
    pyplot.show()
    line = test.readline()
test.close()