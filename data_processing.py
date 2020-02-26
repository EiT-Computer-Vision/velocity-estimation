import numpy as np
import cv2
from frame_functions import getPixelDisplacement
from velocity_estimation import FOCAL_LENGTH, BASELINE, TIME_DELTA


def get_velocity(frame1, frame2):
    # Get disparity maps:
    disparity_map_1 = calculate_disparity_map(frame1.left_img, frame1.right_img)
    disparity_map_2 = calculate_disparity_map(frame2.left_img, frame2.right_img)
    # Get depth maps:
    depth_map_1 = calculate_depth(disparity_map_1)
    depth_map_2 = calculate_depth(disparity_map_2)

    # Find points to track:
    # Will be Nx2 numpy arrays, with pixel coordinates (u,v) per point
    old_pixels, new_pixels = getPixelDisplacement(frame1, frame2)

    # Create arrays for row and column indices, so that we can index all points at the same time:
    old_pixels_row_indices = old_pixels[:, 1]
    old_pixels_column_indices = old_pixels[:, 0]
    new_pixels_row_indices = new_pixels[:, 1]
    new_pixels_column_indices = new_pixels[:, 0]

    # Get the depths on these points:
    depth_points_1 = depth_map_1[old_pixels_row_indices.astype(int), old_pixels_column_indices.astype(int)]
    depth_points_2 = depth_map_2[new_pixels_row_indices.astype(int), new_pixels_column_indices.astype(int)]

    # Add a "-" sign, so that the velocities represent the movement of the car relative to points in forward direction
    # (not points relative to car).

    nonzero_1 = np.nonzero(depth_points_1)
    nonzero_2 = np.nonzero(depth_points_2)
    intersect = np.intersect1d(nonzero_1, nonzero_2)

    # Add a "-" sign, so that the velocities represent the movement of the car relative to points in forward direction
    # (not points relative to car).
    if len(intersect) > 0:
        velocities = -np.divide(depth_points_2[intersect]-depth_points_1[intersect], TIME_DELTA)
    else:
        velocities = 0

    # Return the mean of those velocities (for now):
    return np.mean(velocities)


def calculate_depth(disparity_map):
    # Get global focal length and baseline from the projection matrix:
    focal_length_u = FOCAL_LENGTH
    baseline_x = BASELINE

    # Find depth by dividing baseline times focal length on the disparity
    # for each element in disparity_map which is nonzero:
    depth_map = np.zeros(np.shape(disparity_map))
    np.divide(baseline_x * focal_length_u, disparity_map, out=depth_map, where=disparity_map > 0)

    return depth_map


def calculate_disparity_map(left_img, right_img):
    stereo = cv2.StereoBM_create(numDisparities=48, blockSize=15)
    disparity_map = stereo.compute(left_img, right_img).astype(np.float32)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    disparity_map = cv2.morphologyEx(disparity_map, cv2.MORPH_CLOSE, kernel)
    return disparity_map
