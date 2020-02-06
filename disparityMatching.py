import numpy as np
import cv2
imgL = cv2.imread('./data/2011_09_26/2011_09_26_drive_0096_sync/image_02/data/0000000051.png',0)
imgR = cv2.imread('./data/2011_09_26/2011_09_26_drive_0096_sync/image_03/data/0000000051.png',0)
from imageManipulation import loadData

#baseline = 54 cm?
#focal length = ?


def loadCamToCam(data):
    camToCam = data._load_calib_cam_to_cam('./data/2011_09_26/calib_velo_to_cam.txt','./data/2011_09_26/calib_cam_to_cam.txt')
    return camToCam


def calculate_depth(disparity_map):
    [x,y,_] = np.shape(disparity_map)
    b = 0.54
    f = 5
    depth = np.zeros((x,y),0)
    for i in range(0,x):
        for j in range(0,y):
            if disparity_map[i,j] > 0:
                depth[i,j] = b*f/disparity_map[i,j]


def calculate_disparity_map(img_left, img_right):
    stereo = cv2.StereoBM_create(numDisparities=48, blockSize=15)
    disparity_map = stereo.compute(img_left, img_right).astype(np.float32)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    disparity_map = cv2.morphologyEx(disparity_map, cv2.MORPH_CLOSE, kernel)
    return disparity_map


disparity = calculate_disparity_map(imgL, imgR)
data = loadData()
#cv2.StereoRectify(cameraMatrix1, cameraMatrix2, distCoeffs1, distCoeffs2, imageSize, R, T, R1, R2, P1, P2, Q=None, flags=CV_CALIB_ZERO_DISPARITY, alpha=-1, newImageSize=(0, 0))
#cv2.reprojectImageTo3D(disparity, Q[, _3dImage[, handleMissingValues[, ddepth]]])