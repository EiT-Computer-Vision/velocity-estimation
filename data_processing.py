import numpy as np
import cv2
from math import sqrt
from frame_functions import getPixelDisplacement

# Method for receiving projective matrix - Jens will fix global
# Method for calculating disparity - yep
# Method for getting the depth - yeppsipepsi
# Method for finding the velocity based on depth and points from consecutive frames

def get_error(estimated_velocity, true_velocity):
    # estimated_velocity : float, velocity estimated from clip
    # true_velocity : float, true velocity extracted from metadata
    print(true_velocity)
    print(estimated_velocity)
    error = sqrt((estimated_velocity - true_velocity)**2)
    return error # returns the value

def get_velocity(img1, img2):
    # Get disparity maps:
    # TODO: Get actual two stereo images!

    disparity_map_1 = calculate_disparity_map(img1, img1)
    disparity_map_2 = calculate_disparity_map(img2, img2)
    # Get depth maps:
    depth_map_1 = calculate_depth(disparity_map_1)
    depth_map_2 = calculate_depth(disparity_map_2)

    # Find points to track:
    # Will be Nx2 numpy arrays, with pixel coordinates (u,v) per point
    old_pixels, new_pixels = getPixelDisplacement(img1, img2)

    # Create arrays for row and column indices, so that we can index all points at the same time:
    old_pixels_row_indices = old_pixels[:, 1]
    old_pixels_column_indices = old_pixels[:, 0]
    new_pixels_row_indices = new_pixels[:, 1]
    new_pixels_column_indices = new_pixels[:, 0]

    # Get the depths on these points:
    depth_points_1 = depth_map_1[old_pixels_row_indices.astype(int), old_pixels_column_indices.astype(int)]
    depth_points_2 = depth_map_2[new_pixels_row_indices.astype(int), new_pixels_column_indices.astype(int)]

    # Get time stamps:
    # TODO: Get actual time stamps
    time_1 = 0
    time_2 = 0.1

    # Add a "-" sign, so that the velocities represent the movement of the car relative to points in forward direction
    # (not points relative to car).
    velocities = -(depth_points_2-depth_points_1)/(time_2-time_1)

    # Return the mean of those velocities (for now):
    return np.mean(velocities)


def calculate_depth(disparity_map):
    # Get global projection matrix:
    # TODO: Get the actual matrix
    # Dummy-matrix:
    projection_matrix = np.ones((3, 4))

    # Get focal length and baseline from the projection matrix:
    focal_length_u = projection_matrix[0][0]
    baseline_x = -projection_matrix[0][3]/focal_length_u

    # Fin depth by dividing baseline times focal length on the disparity
    # for each element in disparity_map which is nonzero:
    depth_map = np.zeros(np.shape(disparity_map))
    np.divide(baseline_x * focal_length_u, disparity_map, out=depth_map, where=disparity_map != 0)

    return depth_map


def calculate_disparity_map(img_left, img_right):
    stereo = cv2.StereoBM_create(numDisparities=48, blockSize=15)
    disparity_map = stereo.compute(img_left, img_right).astype(np.float32)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    disparity_map = cv2.morphologyEx(disparity_map, cv2.MORPH_CLOSE, kernel)
    return disparity_map



