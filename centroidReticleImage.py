'''
@title centroidReticleImage
@author: Rebecca Coles
Updated on Nov 3, 2017
Created on Nov 1, 2017

centroidReticleImage
This module holds a series of functions used to find the center of
a reticle from an image.

Modules:
findCentroid
    Take a numpy array of an image and centroid the circles within
    Works: circles = HoughCircles((output/256).astype('uint8'), HOUGH_GRADIENT, 4, 100, 100, 100, minRadius=1, maxRadius=75) #WORKS 11/8/2017
'''

# Import #######################################################################################
from cv2 import HoughCircles, HOUGH_GRADIENT, circle, rectangle, putText, FONT_HERSHEY_SIMPLEX
from numpy import round, copy, uint8, repeat, percentile
from scipy.misc import toimage
from scipy.spatial import distance
################################################################################################

class centroidReticleImage(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def findCentroid(self, image, minRadius, maxRadius, rowsMin, rowsMax, columnsMin, columnsMax):
        '''
        Take a numpy array of an image and centroid the circles within
        '''
        #Copy image
        output = copy(image[rowsMin:rowsMax, columnsMin:columnsMax])
        print('Image dimensions: ', output.shape)
        
        #Image contrast
        #lowerValuePixels = percentile(output, 70)
        #print('Lowest 70%:' + str(lowerValuePixels))
        #higherValuePixels = percentile(output, 95)
        #print('Highest 95%:' + str(higherValuePixels))
            #set contrast
        #[0 for ii in range(output.shape[0]) for jj in range(output.shape[1]) if output[ii,jj] <= lowerValuePixels]
        #[65000 for kk in range(output.shape[0]) for ll in range(output.shape[1]) if output[kk,ll] >= higherValuePixels]
        
        #Find the circles (convert image from uint16 (FITS 16bit) to 8bit)
        circles = HoughCircles((output/256).astype('uint8'), HOUGH_GRADIENT, 4, 100, 100, 100, minRadius, maxRadius) #WORKS 11/8/2017
        #Ensure at least some circles were found
        if circles is not None:
            print('Found circles')
            #Convert the (x, y) coordinates and radius of the circles to integers
            circles = round(circles[0, :]).astype("int")
            #Find the circle closest to the center of the image
                #calculate the  Euclidean distances between two 1-D arrays (circle centers and image center)
            eDist = []
            [eDist.append([distance.euclidean((rowsMax/2, columnsMax/2), (circles[ii][0], circles[ii][1])), ii]) for ii in range(circles.shape[0])]
            minDist = min(eDist[:]) #min Euclidean distance
            correctCircle = circles[minDist[1]][:] #circle corresponding to min Euclidean distance
            #Convert image to RGB
            output.resize((output.shape[0], output.shape[1], 1))
            outputColor = repeat(output.astype(uint8), 3, 2)
            #Loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                #Draw the circle in the output image, then draw a rectangle
                #Corresponding to the center of the circle
                circle(outputColor, (x, y), r, (0, 255, 0), 4)
                rectangle(outputColor, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                putText(outputColor,"Centroid location: " + '(' + str(x) + ',' + str(y) + ') r=' + str(r),
                         (rowsMax-15, 0), FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2)
            #Save Image
            toimage(outputColor, cmin=0.0).save('outfile.png')
        else:
            print('No circles found')