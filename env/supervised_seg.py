import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 

def image_show_plt(img):
    plt.imshow(img)
    plt.show()
    return 

def resize_image(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    return resized
    
def display_histogram(image, xlabel="", ylabel="", title="" ):
    fig, ax = plt.subplots(1, 1)
    ax.hist(image.ravel(), bins=32, range=[0, 256])
    ax.set_xlim(0, 256)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def remove_background(src_img_path):
    # TODO: Check with Silvester why the levels of black in the histogram are still high
    file_name = src_img_path
    src = cv.imread(file_name, 1)
    tmp = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    _,alpha = cv.threshold(tmp,40,255,cv.THRESH_BINARY)
    #split image into blue, green and red array 
    b, g, r = cv.split(src)
    rgba = [b,g,r, alpha]
    dst = cv.merge(rgba,4)
    return dst

def supervised_bin_thresh(srcImg, thresholdVal, higher_val, thres_type):
    img = cv.imread(srcImg, 0)
    __,thresh_img = cv.threshold(img, threshold, higher_val, thres_type)
    # plt.imshow(threshImg,'gray',vmin=0,vmax=255)
    # plt.axis(False)
    # plt.title(title)
    # plt.show()
    return thresh_img

