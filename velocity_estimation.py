"""
Main module containing the program loop. Serves as an entry point to the program.
"""

import display
import glob
import cv2

VIDEO_PATH = "Video data/2011_09_26/2011_09_26_drive_0001_sync/image_00/data"
METADATA_PATH = "Video data/2011_09_26/2011_09_26_drive_0001_sync/oxts/data"


def get_video_sequence(video_path):
    """
    Returns a list of the pahts of all frames in the video.

    Input:
        path - String defining the path to the sequence of frames

    Return:
        video_sequence - List containing the paths of all frames in the sequence as String
    """

    return [frame_path for frame_path in sorted(glob.glob(video_path + "/*.png"))]



def get_video_metadata(metadata_path):

    """
    Returns a list of the metadata.txt files for the current video sequence
    :param metadata_path: file location of the frame metadata
    :return: video_metadata : list containing the metadata of all frames in consecutive order
    """


    return [metadata_path for metadata_path in sorted(glob.glob(metadata_path + "/*.txt"))]



def run(video_path,metadata_path):
    video_sequence = get_video_sequence(video_path)
    video_metadata = get_video_metadata(metadata_path)
    num_frames = len(video_sequence)

    for index, frame in enumerate(video_sequence):
        if index + 1 != num_frames: # we are not at last frame
            img1 = cv2.imread(frame, cv2.IMREAD_GRAYSCALE) # reads the frame as grayscale
            img2 = cv2.imread(video_sequence[index + 1], cv2.IMREAD_GRAYSCALE) # retrieve the next frame in the sequence
            
            metadata = open(video_metadata[index], "r")
            lines = metadata.readlines()
            for line in lines:
                metadata_velocity = float(line.split(" ")[8]) # Real forward velocities
            display.display_velocity(img1, img2, metadata_velocity)


if __name__ == '__main__':
    run(VIDEO_PATH, METADATA_PATH)
