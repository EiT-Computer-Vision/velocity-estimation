import numpy as np
import cv2
from matplotlib import pyplot as plt
imgL = cv2.imread('..\\2011_09_26\\2011_09_26_drive_0096_sync\\image_00\\data\\0000000081.png',0)
imgR = cv2.imread('..\\2011_09_26\\2011_09_26_drive_0096_sync\\image_01\\data\\0000000081.png',0)
from imageManipulation import loadData

def loadCamToCam(data):
    camToCam = data._load_calib_cam_to_cam('..\\2011_09_26\\calib_velo_to_cam.txt',\
    'C:\\Users\\Kjetk\PycharmProjects\\velocityEstimationStereo\\2011_09_26\\calib_cam_to_cam.txt')
    return camToCam
def calculate_disparity_map(img_left, img_right):
    #Returns disparity map seen from right camera (COULD BE WRONG)
    stereo = cv2.StereoBM_create(numDisparities=128, blockSize=15)
    disparity_map = stereo.compute(img_left, img_right).astype(np.float32)

    return disparity_map

def depth_from_disparity(disparity_map,f,B):
    #returns depth in Z-direction from disparity map
    #TODO: scale depth to be in METERS. Unknown scaling factor
    #f is in PIXELS
    # B is in METERS
    #Disparity is in either PIXELS or meters (IDK)
    [x,y] = np.shape(disparity_map)
    In = np.zeros_like(disparity_map)
    pixToM = 0.0002645833
    width = 1242
    for i in range(0,x):
        for j in range(0,y):
            if(disparity_map[i,j] > 0):
                In[i,j] = 2/pixToM*f*B/(disparity_map[i,j]*width)
                print('depth at point (',i,j,') is:', In[i,j], 'meters')
            else:
                continue
    return In

data = loadData()
[x,y] = np.shape(imgL)
camToCam = loadCamToCam(data)

##baseline = 54 cm?
# f = fx = fy = 7.18856e02
#disparity = B*f/Z where Z is depth
#Q on form [1 0 0 -cx; 0 1 0 -cy; 0 0 0 f; 0 0 -1/Tx (cx-cx')/Tx]

baseline = 0.54
focal_length = 719
disparity = calculate_disparity_map(imgL,imgR)
depth_img = depth_from_disparity(disparity,focal_length,baseline)
plt.imshow(depth_img)
plt.show()