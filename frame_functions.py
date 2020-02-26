import cv2
import glob
import numpy as np

# Parameters for the Shi - Tomasi corner detection
FEATURE_PARAMS = dict( maxCorners = 50,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
LK_PARAMS = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 1, 0.03))

def getPixelDisplacement(frame1, frame2):
    # Select features to track
    p0 = cv2.goodFeaturesToTrack(frame1.left_img, **FEATURE_PARAMS)

    # Calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(frame1.left_img, frame2.left_img, p0, None, **LK_PARAMS)

    return np.squeeze(p0), np.squeeze(p1)


def run_test():
    test_images = [img for img in glob.glob("Video data\\2011_09_26\\2011_09_26_drive_0001_sync\\image_00\\data\\*.png")]

    img1 = cv2.imread(test_images[0], cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(test_images[1], cv2.IMREAD_GRAYSCALE)

    init_pixel_pos, new_pixel_pos = getPixelDisplacement(img1, img2)

    print(init_pixel_pos)
    print(new_pixel_pos)
