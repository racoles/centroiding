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
from cv2 import HoughCircles, HOUGH_GRADIENT, circle, rectangle, COLOR_GRAY2RGB, cvtColor
from numpy import round, copy, repeat, uint16
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
        #Find the circles (convert image from uint16 (FITS 16bit) to 8bit)
        circles = HoughCircles((output/256).astype('uint8'), HOUGH_GRADIENT, 4, 100, 100, 100, minRadius, maxRadius) #WORKS 11/8/2017
        #Ensure at least some circles were found
        if circles is not None:
            print('Found circles')
            #Convert the (x, y) coordinates and radius of the circles to integers
            circles = round(circles[0, :]).astype("float")
            #Find the circle closest to the center of the image
                #calculate the  Euclidean distances between two 1-D arrays (circle centers and image center)
            eDist = []
            [eDist.append([distance.euclidean((output.shape[0]/2, output.shape[1]/2), (circles[ii][0], circles[ii][1])), ii]) for ii in range(circles.shape[0])]
            minDist = min(eDist[:]) #min Euclidean distance
            correctCircle = circles[minDist[1]][:] #circle corresponding to min Euclidean distance
            #Convert image to RGB
            #output.resize((output.shape[0], output.shape[1], 1))
            #outputColor = repeat(output.astype(uint16), 3, 2)
            outputColor = cvtColor(output, COLOR_GRAY2RGB)
            #Draw the circle in the output image, then draw a rectangle corresponding to the center of the circle
            circle(outputColor, (int(correctCircle[0]), int(correctCircle[1])), int(correctCircle[2]), (0, 255, 0), 4)
            rectangle(outputColor, (int(correctCircle[0]) - 5, int(correctCircle[1]) - 5), (int(correctCircle[0]) + 5, int(correctCircle[1]) + 5), 
                        (0, 128, 255), -1)
            print("Centroid location: " + '(' + str(correctCircle[0]+rowsMin) + ',' + str(correctCircle[1]+columnsMin) + ') r=' + str(correctCircle[2]))
            #Save Image
            print(outputColor)
            toimage(outputColor, cmin=0.0).save('outfile.png') #cmin=0.0
        else:
            print('No circles found')