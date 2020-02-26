"""
Main module containing the program loop. Serves as an entry point to the program.
"""
import display
import glob
import cv2
from classes import Frame

VIDEO_DIRECTORY_LEFT = "Video data/2011_09_26/2011_09_26_drive_0001_sync/image_00/data"
VIDEO_DIRECTORY_RIGHT = "Video data/2011_09_26/2011_09_26_drive_0001_sync/image_01/data"

# Hardcoded focal length, baseline, time:
# Focal length and time from calib_cam_to_cam.txt:
FOCAL_LENGTH = 7.215377e+02
BASELINE = 3.875744e+02/7.215377e+02
# Circa. Concrete can be gotten from timestamps.txt:
TIME_DELTA = 0.100


def get_video_sequence(path):
    """
    Returns a list of the pahts of all frames in the video.

    Input:
        path - String defining the path to the sequence of frames

    Return:
        video_sequence - List containing the paths of all frames in the sequence as String
    """
    return [frame_path for frame_path in sorted(glob.glob(path + "/*.png"))]


def run(directory_left, directory_right):
    # Initiate frames
    frames = Frame.get_array(directory_left, directory_right)

    # Loop over frames
    for i in range(len(frames)):
        if not frames[i+1].is_last_frame:
            display.display_velocity(frames[i], frames[i+1])


if __name__ == '__main__':
    run(VIDEO_DIRECTORY_LEFT, VIDEO_DIRECTORY_RIGHT)

