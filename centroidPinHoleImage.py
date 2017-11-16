'''
@title centroidPinHoleImage
@author: Rebecca Coles
Updated on Nov 16, 2017
Created on Nov 16, 2017

centroidPinHoleImage
This module holds a series of functions used to find the center of
an illuminated pin hole from an image using code that was adapted
from the IDL Astronomy Users Library.

Compute the centroid of a star using a derivative search (adapted 
for IDL from DAOPHOT, then translated from IDL to Python).
Uses an early DAOPHOT "FIND" centroid algorithm by locating the 
position where the X and Y derivatives go to zero.

Modules:
findCentroid
    Take a numpy array of an image and centroid the pinholes within.
    Compute the centroid of a star using a derivative search 
    (adapted for IDL from DAOPHOT, then translated from IDL to Python).
'''

# Import #######################################################################################
import numpy as np
################################################################################################

class centroidReticleImage(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def findCentroid(self, image, x, y, fwhm):
        '''
        Take a numpy array of an image and centroid the pinholes within
        Compute the centroid of a star using a derivative search 
        (adapted for IDL from DAOPHOT, then translated from IDL to Python).
        
        image  - 2D numpy array
        x,y  -  Integers giving approximate pin hole center
        fwhm -  float value for full-width-half-maximum. The centroid 
                is computed using a box of half width equal to 1.5 sigma = 0.637* fwhm.

        ''' 