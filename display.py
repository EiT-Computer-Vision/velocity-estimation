"""
Module intended to display the data. TBF.
"""
import numpy as np
import cv2
import frame_functions
import data_processing

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

def display_velocity(img1, img2, true_velocity):
    frames = [img1, img2]
    velocity = data_processing.get_velocity(img1, img2)
    error = data_processing.get_error(velocity, true_velocity)

    print(error)
     
    for frame in frames:
        cv2.putText(frame, str(velocity), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(10)

        #print("Current velocity estimate: " + str(velocity))
    return




