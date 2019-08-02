# PYTHON | DATA SCIENCE

# Finding Van Gogh's favorite colors using using k-means clustering on 1000+ paintings. The code to scrape the pictures is included. 

This code was created to a) scrape 1000+ Van Gogh paintings , b)  perform k-means clustering on each painting to identify the dominant colors in each painting and c) perform k-means on the ensemble of clusters from all the images to find Van Gogh's favorite colors.  First run scrapper2.py to scrape/download images and then run main.py function to perform k-means clustering on all images. All the required helper functions are called from main.py . 

The pixel information of each image was transfotmed into three R, G, B vectors prior to performing k-means clustering. 

The final overall cluster centroids were then transformed back to RGB values and plotted to depict Van Gog's favorite colors. Results bellow: 




------------------------------------------------------------------------------------------------------------------------------------------------

![Results Image](https://github.com/fedevillalp/imagecolorclusters/blob/master/picture1.png)

------------------------------------------------------------------------------------------------------------------------------------------------

![Results Image](https://github.com/fedevillalp/imagecolorclusters/blob/master/picture2.png)

------------------------------------------------------------------------------------------------------------------------------------------------

![Results Image](https://github.com/fedevillalp/imagecolorclusters/blob/master/picture3.png)

------------------------------------------------------------------------------------------------------------------------------------------------

![Results Image](https://github.com/fedevillalp/imagecolorclusters/blob/master/picture4.png)


