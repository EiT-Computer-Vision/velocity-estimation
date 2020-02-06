import cv2
import numpy as np
import glob
import disparityMatching

imgLeft_array = []
imgRight_array = []
for (fileLeft, fileRight) in zip(glob.glob('./data/2011_09_26/2011_09_26_drive_0096_sync/image_02/data/*.png'),
 ('./data/2011_09_26/2011_09_26_drive_0096_sync/image_03/data/*.png')):
    imgLeft = cv2.imread(fileLeft)
    print('read one image')
    imgRight = cv2.imread(fileRight)
    print('read second image')
    height, width, layers = imgLeft.shape
    size = (width, height)
    disparityMatching.calculate_disparity_map(imgLeft, imgRight)
    imgLeft_array.append(imgLeft)
    imgRight_array.append(imgRight)

out = cv2.VideoWriter('./videos/disparity.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(imgLeft_array)):
    out.write(imgLeft_array[i])
out.release()