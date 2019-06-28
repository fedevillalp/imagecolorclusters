# -*- coding: utf-8 -*-
"""
Federico Villalapndo 6/28/2019
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import PIL
import scipy
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import numpy as np


#image = plt.imread('./dataquest.jpg')
image = plt.imread('./test3.jpg')
plt.imshow(image)


r = []
g = []
b = []

for line in image:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

#print(len(r), len(g), len(b))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r, g, b)
ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')

d = {'r': r, 'g': g,'b': b}
pandaDataFrame = pd.DataFrame(data=d)


pandaDataFrame['scaled_red'] = whiten(pandaDataFrame['r'])
pandaDataFrame['scaled_green'] = whiten(pandaDataFrame['g'])
pandaDataFrame['scaled_blue'] = whiten(pandaDataFrame['b'])

#print(pandaDataFrame.sample(n = 5))

x = kmeans(pandaDataFrame[['scaled_red', 'scaled_green', 'scaled_blue']], 6)
cluster_centers = x[0]
print("CLUSTER CENTERS:",cluster_centers)

r_std, g_std, b_std = pandaDataFrame[['r', 'g', 'b']].std()
#
colors = []

for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    #print(cluster_center)
    colors.append((scaled_r * r_std / 255, scaled_g * g_std / 255, scaled_b * b_std / 255))

print("COLORS:",colors)

plt.figure()
plt.imshow([colors])
plt.show()


