'''
@title centroidReticleImage
@author: Rebecca Coles
Updated on Nov 2, 2017
Created on Nov 1, 2017

centroidReticleImage
This module holds a series of functions used to find the center of
a reticle from an image.

Modules:
findCentroid
    Take a numpy array of an image and centroid the circles within
'''

# Import #######################################################################################
from cv2 import HoughCircles, HOUGH_GRADIENT, circle, rectangle, imshow, waitKey, putText, FONT_HERSHEY_SIMPLEX
from numpy import round, hstack, copy
from loadingImages import loadingImages
################################################################################################

class centroidReticleImage(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def findCentroid(self, image, minRadius):
        '''
        Take a numpy array of an image and centroid the circles within
        '''
        #Flatten image
        print(image.shape)
        output = copy(image)
        #Convert image from uint16 (FITS 16bit) to 8bit
        display_min = 1000
        display_max = 10000
        im = loadingImages()
        output = im.convert16to8bit(output, display_min, display_max)
        print(output.dtype)
        #Find the circles
        circles = HoughCircles(image, HOUGH_GRADIENT, 1.2, minRadius)
        #Ensure at least some circles were found
        if circles is not None:
            #Convert the (x, y) coordinates and radius of the circles to integers
            circles = round(circles[0, :]).astype("int")
            
            #Loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                #Draw the circle in the output image, then draw a rectangle
                #Corresponding to the center of the circle
                circle(output, (x, y), r, (0, 255, 0), 4)
                rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                putText(output,"Centroid locations: " + '(' + str(x) + ',' + str(y) + ') r=' + str(r),
                         (0,0), FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2)
                
            # show the output image
            imshow("output", hstack([image, output]))
            waitKey(0)