"""
Main module containing the program loop. Serves as an entry point to the program.
"""

import display
import glob
import cv2

velocity_PATH = "C:\\Users\Masoud\\Desktop\\Semester 2\\Eit - Computer Vision\\2011_09_26_drive_0001_sync\\oxts\\data"


""" get_video_sequence(path)---> get_velocity   """

def get_velocity(path):

    return [velo_path for velo_path in sorted(glob.glob(path + "/*.txt"))]



def run(path):
    velocity = get_velocity(path)
    num_velo = len(velocity)

    for index, velocity in enumerate(velocity):
        if index + 1 != num_velo: # we are not at last frame
            f = open(velocity, "r")
            lines = f.readlines()

            for line in lines:
                vars = line.split(" ")
                print(vars[8])


if __name__ == '__main__':
    run(velocity_PATH)
