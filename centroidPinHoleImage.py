'''
@title centroidPinHoleImage
@author: Rebecca Coles
Updated on Nov 16, 2017
Created on Nov 16, 2017

centroidPinHoleImage
This module holds a series of functions used to find the center of
an illuminated pin hole from an image using code that was originally
from the IDL Astronomy Users Library.

Modules:
findCentroid
    Take a numpy array of an image and centroid the pinholes within.
    This code is from the IDL Astronomy Users Library.
'''

# Import #######################################################################################
import numpy as np
################################################################################################

class centroidReticleImage(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def findCentroid(self, image, minRadius, maxRadius, rowsMin, rowsMax, columnsMin, columnsMax):
        '''
        Take a numpy array of an image and centroid the pinholes within
        This code is from the IDL Astronomy Users Library
        ''' 