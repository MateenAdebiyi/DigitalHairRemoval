import numpy as np
import cv2
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    #get alpha and beta values
    alpha, beta =2, -420
    # get directory path where the images are stored
    image_dir = "/Users/aaangd/DigitalHairRemoval/inputImages2/"
    # get directory path where you want to save the images
    output_dir = "/Users/aaangd/DigitalHairRemoval/outputImages2/"
    kernel = cv2.getStructuringElement(1,(17,17))
    #ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
    #iterate through all the files in the image directory
    for _, _, image_names in os.walk(image_dir):
        #iterate through all the files in the image_dir
      
        for image_name in image_names:
              #print (image_names)
    
            # check for extension .jpg
            if '.jpg' in image_name:
                # get image read path(path should not contain spaces in them)
                filepath = os.path.join(image_dir, image_name)
                # get image write path
                dstpath = os.path.join(output_dir, image_name)
                print(filepath, dstpath)
                # read the image
                image = cv2.imread(filepath)
                # do your processing
               # image2 = cv2.addWeighted(image, alpha,np.zeros_like(image),0,beta)
                grayScale = cv2.cvtColor( image, cv2.COLOR_RGB2GRAY )
                blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
                ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
                dst = cv2.inpaint(image,thresh2,1,cv2.INPAINT_TELEA)
                #hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
                # write the image in a different path with the same name
                cv2.imwrite(dstpath, dst)
                #print(image.shape, image2.shape, hsv.shape)

    
