# @SciView sv

from net.imglib2 import RealPoint
from jarray import array
import random as random

w = 1.0
h = w
d = w

num_spots = 10
spotR = 3

def rand_spot():
    coord = [random.random() * w - w * 0.5, random.random() * h - h * 0.5, random.random() * d - d * 0.5]
    return RealPoint(array(coord, 'd'))

spots = [rand_spot() for k in range(num_spots)]

print(spots)
print(spots[0])

sv.addPointCloud(spots)
