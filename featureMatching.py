import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread('./data/2011_09_26/2011_09_26_drive_0096_sync/image_02/data/0000000000.png',0)
img2 = cv.imread('./data/2011_09_26/2011_09_26_drive_0096_sync/image_02/data/0000000001.png',0)
# Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
i = 0
for m in matches:
    print(m.distance)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()