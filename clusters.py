from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import matplotlib.pyplot as plt
import pandas as pd
import helper


def get_dominant_colors(image_file_name,k):
    # OPEN IMAGE FILE (Image is array with the dimensions M x N x 3)
    image = plt.imread(image_file_name)                     
    plt.imshow(image)                                       # SHOW IMAGE             
    
    # GET IMAGE R,G,B PIXEL VALUES (3 lists one per color)                      
    red, green, blue = helper.get_image_RGB_values(image)   
    helper.plot3d(red,green,blue,'R','G','B')               # PLOT IMAGE R,G,B PIXEL VALUES (3D plot - 1 pixel per point)
    rgb_data = {'red':red, 'green':green, 'blue': blue}     # PUT R,G,B PIXEL VALUES INTO DATA FRAME
    image_dataFrame = pd.DataFrame(data=rgb_data)           # ""
    
     # STANDARDIZE R,G,B PIXEL VALUES
    image_dataFrame['scaled_red'] = whiten(image_dataFrame['red'])
    image_dataFrame['scaled_green'] = whiten(image_dataFrame['green'])
    image_dataFrame['scaled_blue'] = whiten(image_dataFrame['blue'])
    
    # PERFORM K-MEANS CLUSTERING ON IMAGE R,G,B PIXEL VALUES
    clusters = kmeans(image_dataFrame[['scaled_red', 'scaled_green', 'scaled_blue']], k)
    
    #TRANSFORM CLUSTER CENTERS TO 0-1 COLOR SCALE and PLOT
    colors = helper.cluster_centers_to_0_1_scale(image_dataFrame, clusters)
    helper.plot_cluster_colors(colors)
    
    print(image_dataFrame.sample(n = 5))   

    return colors                 




#-------------------------------------------------------------------------------------
#Algorithm:	
#Clusters the data into k groups where k  is predefined.
#Select k points at random as cluster centers.
#Assign objects to their closest cluster center according to the Euclidean distance function.
#Calculate the centroid or mean of all objects in each cluster.
#Repeat steps 2, 3 and 4 until the same points are assigned to each cluster in consecutive rounds.
 