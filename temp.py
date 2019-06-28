# -*- coding: utf-8 -*-
"""
by Federico Villalapndo 6/28/2019

Reference: 
https://www.dataquest.io/blog/tutorial-colors-image-clustering-python/
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import PIL
import scipy
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import numpy as np

# OPEN IMAGE FILE
image = plt.imread('./test2.jpg')
plt.imshow(image)

# GET THE IMAGE R, G, B VALUES
r = []
g = []
b = []

for line in image:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

# PLOT THE IMAGE PIXELS IN R, G, B,  0-255 SPACE
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r, g, b)
ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')

# CREATE PANDA DATA FRAME
d = {'r': r, 'g': g,'b': b}
pandaDataFrame = pd.DataFrame(data=d)

# STANDARDIZE R,G,B PIXEL DATA
pandaDataFrame['scaled_red'] = whiten(pandaDataFrame['r'])
pandaDataFrame['scaled_green'] = whiten(pandaDataFrame['g'])
pandaDataFrame['scaled_blue'] = whiten(pandaDataFrame['b'])
#print(pandaDataFrame.sample(n = 5))

# PERFORM K-MEANS CLUSTERING ON IMAGE R,G,B PIXEL INFORMATION
x = kmeans(pandaDataFrame[['scaled_red', 'scaled_green', 'scaled_blue']], 6)
cluster_centers = x[0]
print("CLUSTER CENTERS:",cluster_centers)

# ADD STANDARDIZED INFORMATION TO DATAFRAME
r_std, g_std, b_std = pandaDataFrame[['r', 'g', 'b']].std()
colors = []

# GET COLOR CENTERS, MULTIPLY BY STD TO BRING BACK TO 0-255 AND NORMALIZE TO GO INTO 0-1 RANGE
for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    #print(cluster_center)
    colors.append((scaled_r * r_std / 255, scaled_g * g_std / 255, scaled_b * b_std / 255))

#PLOT THE COLORS RESULTING FROM K-MEANS CLUSTERING
print("COLORS:",colors)
plt.figure()
plt.imshow([colors])
plt.show()




