import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import urllib.request as request
import preprocessing as pp


def first_method_thresholding(src):
    g = pp.get_green_channel(src)
    smooth = pp.smooth_image(g)
    enhanced = pp.enhance_image(smooth)
    # return_val, thresh_img = cv.threshold(smooth, 100, 255, v.THRESH_BINARY_INV+cv.THRESH_OTSU)
    th3 = cv.adaptiveThreshold(enhanced,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY,11,2)
    return th3

def second_method_active_contours(src):
    # pre-processing            #TODO: today 
    # active conoturs 
    pass

def third_method_random_walker(src):         # TODO: tomorrow 
    # pre_processing 
    # random walker
    pass

def display_histogram(grey_image, xlabel="", ylabel="", title="" ):
    fig, ax = plt.subplots(1, 1)
    ax.hist(grey_image.ravel(), bins=32, range=[0, 256])
    ax.set_xlim(0, 256)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

