'''
@title centroidPinHoleImage
@author: Rebecca Coles
Updated on Nov 16, 2017
Created on Nov 16, 2017

centroidPinHoleImage
This module holds a series of functions used to find the center of
an illuminated pin hole from an image.

Modules:
findCentroid
    Take a numpy array of an image and centroid the pinholes within
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
        Take a numpy array of an image and centroid the pinholes within
        ''' 