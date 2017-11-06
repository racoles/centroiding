'''
@title centroiding
@author: Rebecca Coles
Updated on Nov 1, 2017
Created on Nov 1, 2017

centroiding
This project is used to find the center of various circles present in an image.
'''

# Import #######################################################################################
from loadingImages import loadingImages
from centroidReticleImage import centroidReticleImage
################################################################################################

if __name__ == '__main__':
    im = loadingImages()
    cr = centroidReticleImage()
    
    images, _ = im.openAllFITSImagesInDirectory()
    circles = cr.findCentroid(images[0], 1, 80, 390, 580, 300, 500) #(image, minRadius, maxRadius, rowsMin, rowsMax, columnsMin, columnsMax)