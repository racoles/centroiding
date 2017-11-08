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
from numpy import array
from astropy.nddata import CCDData
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