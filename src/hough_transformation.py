import numpy
from PIL import Image
from math import cos, sin, floor


def is_white(pixel):
    return pixel[0] == pixel[1] == pixel[2] == 255


path = 'data/e2.png'
r = 55
fi_max, fi_min = 360, 0
img = Image.open(path)
np_img = numpy.array(img)
height, width, _ = np_img.shape
H = numpy.zeros((height, width), dtype=int)

for x in range(height):
    print(str(int(x/height * 100)) + "%")
    for y in range(width):
        if is_white(np_img[x][y]):
            for fi in range(fi_min, fi_max):
                a = x - floor(r * cos(fi))
                b = y + floor(r * sin(fi))
                if 0 < a < height and 0 < b < width:
                    H[a][b] += 1

R = numpy.zeros((height, width, 3), dtype=numpy.uint8)

for x in range(height):
    for y in range(width):
        R[x][y] = [255, 255 - H[x][y], 255]

img = Image.fromarray(R, 'RGB')
img.show()
