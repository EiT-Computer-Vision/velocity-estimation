import numpy as np
import cv2
from frame_functions import getPixelDisplacement

# Method for receiving projective matrix - Jens will fix global
# Method for calculating disparity - yep
# Method for getting the depth - yeppsipepsi
# Method for finding the velocity based on depth and points from consecutive frames


def get_velocity(img1, img2):
    # Get disparity maps:
    disparity_map_1 = calculate_disparity_map(img1[0], img1[1])
    disparity_map_2 = calculate_disparity_map(img2[0], img2[1])
    # Get depth maps:
    depth_map_1 = calculate_depth(disparity_map_1)
    depth_map_2 = calculate_depth(disparity_map_2)

    # Find points to track:
    old_pixels, new_pixels = getPixelDisplacement(img1, img2)

    # TODO: Find depth on these points in consecutive frames and get the velocity




def calculate_depth(disparity_map):
    # Get global projection matrix:
    projection_matrix = np.ndarray((3, 4), np.zeros((3, 4)))

    # Get focal length and baseline from the projection matrix:
    focal_length_u = projection_matrix[0][0]
    baseline_x = -projection_matrix[0][3]/focal_length_u

    # Fin depth by dividing baseline times focal length on the disparity
    # for each element in disparity_map which is nonzero:
    depth_map = np.divide(baseline_x * focal_length_u, disparity_map, where= disparity_map != 0)

    return depth_map


def calculate_disparity_map(img_left, img_right):
    stereo = cv2.StereoBM_create(numDisparities=48, blockSize=15)
    disparity_map = stereo.compute(img_left, img_right).astype(np.float32)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    disparity_map = cv2.morphologyEx(disparity_map, cv2.MORPH_CLOSE, kernel)
    return disparity_map
