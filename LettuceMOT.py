from matplotlib import image
from matplotlib import pyplot
import numpy
from PIL import Image
import PIL
import cv2
import os
import glob

test = open('B&F2\gt.txt') #change the 2 to 1 when cropping a B&F1
line = test.readline()
img_dir = "B&F2\img" #change the 2 to 1 when cropping a B&F1
crop_dir = "cropped 2" #change the 2 to 1 when cropping a B&F1
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
photos = []
for f1 in files:
    img = cv2.imread(f1)
    photos.append(img)
while line:
    print(line)
    data = line.split(',')
    imgid = data[0]
    letid = data[1]
    xcor = data[2]
    ycor = data[3]
    width = data[4]
    height = data[5]
    imgiduse = int(imgid) - 1
    im = photos[imgiduse]
    xuse = int(xcor)
    yuse = im.shape[0] - int(ycor)
    widuse = xuse + int(width)
    heuse = yuse - int(height)
    print(imgid, letid, xcor, ycor, width, height)
    print(xuse, heuse)
    print(widuse, yuse)
    cropped = im[heuse:yuse, xuse:widuse]
    tosave = Image.fromarray(cropped)
    filename = imgid + '-' + letid
    tosave.save(f"{crop_dir}/{filename}.png")
    line = test.readline()
test.close()