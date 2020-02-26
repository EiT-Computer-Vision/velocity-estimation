"""
Main module containing the program loop. Serves as an entry point to the program.
"""

import display
import glob
import cv2

VIDEO_PATH = "Video data/2011_09_26/2011_09_26_drive_0001_sync/image_00/data"
VELOCITY_PATH = "C:\\Users\Masoud\\Desktop\\Semester 2\\Eit - Computer Vision\\2011_09_26_drive_0001_sync\\oxts\\data"


def get_video_sequence(video_path):
    """
    Returns a list of the pahts of all frames in the video.

    Input:
        path - String defining the path to the sequence of frames

    Return:
        video_sequence - List containing the paths of all frames in the sequence as String
    """
    return [frame_path for frame_path in sorted(glob.glob(video_path + "/*.png"))]



def get_metadata_velocity(metadata_path):
    
    return [velo_path for velo_path in sorted(glob.glob(metadata_path + "/*.txt"))]



def run(video_path,metadata_path):
    video_sequence = get_video_sequence(video_path)
    metadata_velocity = get_metadata_velocity(metadata_path)
    num_frames = len(video_sequence)
    num_velo = len(metadata_velocity)

    for index, frame in enumerate(video_sequence):
        if index + 1 != num_frames: # we are not at last frame
            img1 = cv2.imread(frame, cv2.IMREAD_GRAYSCALE) # reads the frame as grayscale
            img2 = cv2.imread(video_sequence[index + 1], cv2.IMREAD_GRAYSCALE) # retrieve the next frame in the sequence
            
            metadata = open(metadata_velocity[index], "r")
            lines = metadata.readlines()
            for line in lines:
                Forward_velocity = float(line.split(" ")[8]) # Real forward velocities
            display.display_velocity(img1, img2, Forward_velocity)
            



    


if __name__ == '__main__':
    run(VIDEO_PATH,VELOCITY_PATH)
