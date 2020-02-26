"""
Module intended to display the data. TBF.
"""
import numpy as np
import cv2
import frame_functions
from data_processing import get_velocity

def get_velocity_dummy(frame1, frame2):
    """
    Dummy function that calculates pixel velocity without depth perception. Only to be used for testing.
    :param frame1:
    :param frame2:
    :return: mean velocity of all points
    """
    init_pos, new_pos = frame_functions.getPixelDisplacement(frame1.left_img, frame2.left_img)
    component_displacement = new_pos - init_pos
    total_displacement = np.sqrt(np.sum(np.square(component_displacement), axis=1))
    velocity = total_displacement/0.1
    return np.mean(velocity)


def display_velocity(frame1, frame2):
    frames = [frame1, frame2]
    velocity = get_velocity(frame1, frame2)

    for frame in frames:
        cv2.putText(frame.left_img, str(velocity), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame.left_img)
        cv2.waitKey(10)

        #print("Current velocity estimate: " + str(velocity))
    return




