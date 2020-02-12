"""
Module intended to display the data. TBF.
"""

import frame_functions
import numpy as np

def get_velocity_dummy(img1, img2):
    """
    Dummy function that calculates pixel velocity without depth perception. Only to be used for testing.
    :param img1:
    :param img2:
    :return: mean velocity of all points
    """
    init_pos, new_pos = frame_functions.getPixelDisplacement(img1, img2)
    component_displacement = new_pos - init_pos
    total_displacement = np.sqrt(np.sum(np.square(component_displacement), axis=1))
    velocity = total_displacement/0.1
    return np.mean(velocity)

def display_velocity(img1, img2):
    velocity= get_velocity_dummy(img1, img2)
    print("Current velocity estimate: " + str(velocity))





