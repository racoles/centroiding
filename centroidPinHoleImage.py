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
    
    Maximum pixel within distance from input pixel X, Y  determined
    from FHWM is found and used as the center of a square, within
    which the centroid is computed as the value (XCEN,YCEN) at which
    the derivatives of the partial sums of the input image over (y,x)
    with respect to (x,y) = 0.  In order to minimize contamination from
    neighboring stars stars, a weighting factor W is defined as unity in
    center, 0.5 at end, and linear in between.
    
    Values for xcen and ycen will not be computed if the computed
    centroid falls outside of the box, or if the computed derivatives
    are non-decreasing.   If the centroid cannot be computed, then a 
    xcen and ycen are set to -1 and a message is displayed.
'''

# Import #######################################################################################
import numpy as np
################################################################################################

class centroidReticleImage(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def findCentroid(self, image, x, y, fwhm, extendbox = False):
        '''
        Take a numpy array of an image and centroid the pinholes within
        Compute the centroid of a star using a derivative search 
        (adapted for IDL from DAOPHOT, then translated from IDL to Python).
        
        image  - 2D numpy array
        x,y  -  Integers giving approximate pin hole center
        fwhm -  float value for full-width-half-maximum. The centroid 
                is computed using a box of half width equal to 1.5 sigma = 0.637* fwhm.
        extendbox -  {non-negative positive integer}.   CNTRD searches a box with
                       a half width equal to 1.5 sigma  = 0.637* FWHM to find the
                       maximum pixel.    To search a larger area, set extendbox to
                       the number of pixels to enlarge the half-width of the box.
                       A list/array of [X,Y] coordinates defines a rectangle.
                       Default is 0; prior to June 2004, the default was extendbox = 3
        ''' 