'''
@title loadingImages
@author: Rebecca Coles
Updated on Nov 1, 2017
Created on Nov 1, 2017

loadingImages
This module holds a series of functions that I use to handle
various file creation/manipulation/etc.

Modules:
openFile
    This function creates an open file dialogue box and returns the name of the user selected file.
openDir
    This function creates an open directory dialogue box and returns the name of the user selected directory.
getFileNameFromPath
    Extract filenames from paths, no matter what the operating system or path format is from.
openAllFITSImagesInDirectory
    This function convertsFITs type images to a 4D array.
'''

# Import #######################################################################################
from tkinter import filedialog
from ntpath import split, basename
from glob import glob
from astropy.io import fits
from numpy import array, floor_divide, uint8, take, arange
################################################################################################

class loadingImages(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def openFile(self):
        '''
        Create open file dialogue box
        '''
        return filedialog.askopenfilename()
    
    def openDir(self):
        '''
        Create open directory dialogue box
        '''
        return filedialog.askdirectory()
    
    def getFileNameFromPath(self, path):
        '''
        Extract filenames from paths, no matter where the operating system or path format is from
        '''
        head, tail = split(path)
        return tail or basename(head)
    
    def openAllFITSImagesInDirectory(self):
        '''
        Open multiple images and save them to a numpy array
        '''
        #open image file
        dirPath = loadingImages()
        try:
            dirLocation = dirPath.openDir()
        except IOError:
            print('The directory could not be opened, or no directory was selected.')
        filelist = glob(dirLocation + '/*.*')
        fitsImages = [fits.getdata(image) for image in filelist]
        #convert to 4D numpy array
        return array(fitsImages), filelist
    
    def _convert16to8bit(self, image, display_min, display_max): 
        # Here I set copy=True in order to ensure the original image is not
        # modified. If you don't mind modifying the original image, you can
        # set copy=False or skip this step.
        image = array(image, copy=True)
        image.clip(display_min, display_max, out=image)
        image -= display_min
        floor_divide(image, (display_max - display_min + 1) / 256,
                    out=image, casting='unsafe')
        return image.astype(uint8)
    
    def convert16to8bit_LUT(self, image, display_min, display_max) :
        '''
        Look Up Table for convert16to8bit. Makes convert16to8bit twice as fast
        '''
        lut = arange(2**16, dtype='uint16')
        lut = self._convert16to8bit(lut, display_min, display_max)
        return take(lut, image)
        #Look Up Table for convert16to8bit. Makes convert16to8bit twice as fast