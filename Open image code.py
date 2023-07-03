
from matplotlib import image
from matplotlib import pyplot
image = image.imread('E:\Maybe\8a2c974a-8683-4936-9752-348b4142d418.jpg')
print(image.dtype)
print(image.shape)
pyplot.imshow(image)
pyplot.show()