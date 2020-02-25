import matplotlib.pyplot as plt
from math import *
from random import choice
from randomw import RandomWalk


obj = RandomWalk(1000)
obj.generate()
plt.scatter(obj.x_, obj.y_ ,  edgecolors="red")

plt.show()