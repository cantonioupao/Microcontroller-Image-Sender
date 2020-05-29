import numpy as np
from matplotlib import pyplot as plt
from imageio import imread # Need 'Imageio' 'Pillow' packages
import cv2
from math import floor, ceil

def prep_img(img_name, x_size=32, y_size=32, *img_position):
    image_read = imread(img_name)
    image_test = np.asarray(image_read)
    final_image = cv2.resize(image_test, (x_size, y_size))
        

    return final_image
    
