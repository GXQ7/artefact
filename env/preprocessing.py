import cv2 as cv
import numpy as np


def load_coloured_img(src_img_path):
    img = cv.imread(src_img_path, 1)
    return img

def convert_greyscale(colour_img):
    greyscale_img = cv.cvtColor(colour_img, cv.COLOR_BGR2GRAY)
    return greyscale_img

def get_green_channel(src_img):
    green_channel = src_img[:, :, 1]
    return green_channel
    
def enhance_image(img):
    clahe = cv.createCLAHE(clipLimit=1.3, tileGridSize=(4,4)) 
    cl1 = clahe.apply(img)
    return cl1

def smooth_image(src): 
    img_blurred = cv.medianBlur(src, 5) 
    return img_blurred



