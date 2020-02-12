"""
Main module containing the program loop. Serves as an entry point to the program.
"""

import displacement
import glob
import cv2

VIDEO_PATH = "Video data\\2011_09_26\\2011_09_26_drive_0001_sync\\image_00\\data"


def get_video_sequence(path):
    """
    Returns a list of the pahts of all frames in the video.

    Input:
        path - String defining the path to the sequence of frames

    Return:
        video_sequence - List containing the paths of all frames in the sequence as String
    """
    return [frame_path for frame_path in glob.glob(path + "\\*.png")]

def get_next_frames(video_sequence):

def run():
    video_sequence = get_video_sequence(VIDEO_PATH)
    num_frames = len(video_sequence)

    for index, frame in enumerate(video_sequence):
        if index + 1 != num_frames: # we are not at last frame
            img1 = cv2.imread(frame, cv2.IMREAD_GRAYSCALE) # reads the frame as grayscale
            img2 = cv2.imread(video_sequence[index + 1], cv2.IMREAD_GRAYSCALE) # retrieve the next frame in the sequence

run()