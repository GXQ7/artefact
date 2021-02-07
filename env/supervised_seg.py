import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import urllib.request as request

def load_coloured_img(src_img_path):
    #opencv defaults to bgr colour order for images - needs changed if displaying with matplotlib
    img_bgr = cv.imread(src_img_path)
    return img_bgr

def convert_greyscale(colour_img):
    greyscale_img = cv.cvtColor(colour_img, cv.COLOR_BGR2GRAY)
    return greyscale_img

#TODO:
def smooth_image():
    pass

def enhance_image():
    pass
  
#----------------------------------------------------------------------------------------------------------

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
    
def display_histogram(grey_image, xlabel="", ylabel="", title="" ):
    fig, ax = plt.subplots(1, 1)
    ax.hist(image.ravel(), bins=32, range=[0, 256])
    ax.set_xlim(0, 256)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def remove_background(src_img, grey_image):
    # TODO: Check with Silvester why the levels of black in the histogram are still high
    _,alpha = cv.threshold(grey_image,100,255,cv.THRESH_BINARY)
    #split image into blue, green and red array 
    blue, green, red = cv.split(src_img)
    bgra = [blue, green, red, alpha]
    dst = cv.merge(bgra,4)
    return dst

def supervised_bin_thresh(srcImg, thresholdVal, higher_val, thres_type):
    img = cv.imread(srcImg, 0)
    __,thresh_img = cv.threshold(img, threshold, higher_val, thres_type)
    # plt.imshow(threshImg,'gray',vmin=0,vmax=255)
    # plt.axis(False)
    # plt.title(title)
    # plt.show()
    return thresh_img


def url_to_img(url):
    #download image, convert to numpy array and read into opencv format
    resp = request.urlretrieve(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image)
    return image


  
img = load_coloured_img("C:/Users/gquin/Desktop/artefact/env/GlaucomaImages/001.jpg")
resized = resize_image(img, 20)
greyimg = convert_greyscale(resized)
# removed = remove_background(img, greyimg)
cv.imshow('Glaucoma Image 001', greyimg)
cv.waitKey(0)