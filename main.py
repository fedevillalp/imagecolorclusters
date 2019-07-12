"""
@author: federico
"""
import os
import helper
import clusters
from scipy.cluster.vq import kmeans

directory = '/Users/federico/Library/Mobile Documents/com~apple~CloudDocs/Personal Federico [iCloud]/Projectos/Data Science/PicassoFinal'
dominant_colors_all = []
k_painting = 6
k_overall = 10


#EXTACT DOMINANT COLORS FROM EACH PAINTING (.JPG OR .PNG) IN FOLDER
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        print(filename)
        dominant_colors = clusters.get_dominant_colors(filename, k_painting)
        dominant_colors_all.append(dominant_colors)

all_paintings_dataFrame = helper.make_dataframe(dominant_colors_all)
print(all_paintings_dataFrame)


#PERFORM K-MEANS ON THE CONSOLIDATED DOMINANT COLORS OF ALL PAINTINGS
cluster_centers_all = kmeans(all_paintings_dataFrame[['r_all', 'g_all', 'b_all']],k_overall)
print('Final Color Clusters for all paintings: ', cluster_centers_all[0])
helper.plot_cluster_colors(cluster_centers_all[0])
