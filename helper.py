import pandas as pd
import matplotlib.pyplot as plt
    
#EXTRACTS RGB VALUES FROM IMAGE FILE
def get_image_RGB_values(image):
    r = []
    g = []
    b = []
    for line in image:
        for pixel in line:
            temp_r, temp_g, temp_b = pixel  #Extract R,G,B from pixel vector
            r.append(temp_r)                #Vector of all the R values in image
            g.append(temp_g)                #Vector of all the G values in image
            b.append(temp_b)                #Vector of all the B values in image
    return r,g,b
   
#TRANSFORMS CLUSTER CENTERS TO 0-1 COLOR SCALE
def cluster_centers_to_0_1_scale(image_dataFrame, clusters):
    colors = []
    cluster_centers = clusters[0]

    # GET STANDARD DEVIATION FROM R,G,B lists in DATAFRAME
    r_std, g_std, b_std = image_dataFrame[['red', 'green', 'blue']].std()
    
    # GET COLOR CENTERS, MULTIPLY BY STD TO BRING BACK TO 0-255 AND NORMALIZE TO GO INTO 0-1 RANGE
    for cluster_center in cluster_centers:
        scaled_r, scaled_g, scaled_b = cluster_center
        colors.append((scaled_r * r_std / 255, scaled_g * g_std / 255, scaled_b * b_std / 255))
    
    return colors

#PLOT THE COLORS RESULTING FROM K-MEANS CLUSTERING
def plot_cluster_colors(colors):
    plt.figure()
    plt.imshow([colors])
    plt.show()
    
 # PLOTS 3 VECTORS IN 3D
def plot3d(x,y,z,x_label,y_label,z_label):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)

 # MAKE DATAFRAME
def make_dataframe(dominant_colors_all):
    r_all = []
    g_all = []
    b_all = []
    for painting in dominant_colors_all:
        for color in painting:
            r_temp,g_temp,b_temp = color
            r_all.append(r_temp)
            g_all.append(g_temp)
            b_all.append(b_temp)
    d_all = {'r_all': r_all, 'g_all': g_all,'b_all': b_all}
    all_paintings_dataFrame = pd.DataFrame(data=d_all)
    return all_paintings_dataFrame



