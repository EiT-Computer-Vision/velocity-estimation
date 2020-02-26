import glob
import cv2


# Class for holding frame data. Could be extended to hold timestamps.
class Frame:
    # Will make a Frame object from left and right image path.
    # If only one channel wanted, just pass the left_path parameter.
    # Default here is grayscale. If colored, set is_grayscale = False.
    def __init__(self, left_path, right_path=None, is_grayscale=True, is_last_frame=False):
        if is_grayscale:
            self.left_img = cv2.imread(left_path, cv2.IMREAD_GRAYSCALE)
            self.right_img = cv2.imread(right_path, cv2.IMREAD_GRAYSCALE) if right_path else None
        else:
            self.left_img = cv2.imread(left_path)
            self.right_img = cv2.imread(right_path) if right_path else None
        self.is_last_frame = is_last_frame

    # Will make an array of frame objects from directories holding all png files.
    # If only one channel wanted, pass only into left_directory parameter.
    @classmethod
    def get_array(cls, left_directory, right_directory=None):
        left_paths = [frame_path for frame_path in sorted(glob.glob(left_directory + "/*.png"))]
        right_paths = [frame_path for frame_path in sorted(glob.glob(right_directory + "/*.png"))] if right_directory else None
        frames = [Frame(left, right) for left, right in zip(left_paths, right_paths)]
        frames[-1] = Frame(left_paths[-1], right_paths[-1], is_last_frame=True)
        return frames
