import preprocessing as pp
import cv2 as cv
import supervised_segmentation as ss
import matplotlib.pyplot as plt

rgb_test = pp.load_coloured_img("GlaucomaImages/001.jpg")
grey_test = pp.convert_greyscale(rgb_test)

def show(img):
    resized = ss.resize_image(img, 30)
    cv.imshow('Image', img)
    cv.waitKey(0)
    return


#pre_processing
img = cv.cvtColor(rgb_test, cv.COLOR_BGR2RGB)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
g = pp.get_green_channel(img)
blur = cv.medianBlur(g, 5)
enhance = pp.enhance_image(g)
ss.display_histogram(enhance, "bins", "frequency of bins", "Histogram of CLAHE enhanced image")


# display pre-processing techniques
# titles = ['Original', 'Grey Scale','Green Channel', 'Median Blur','CLAHE Enhanced']
# images = [img, grey, g, blur, enhance]
# for i in range(5):
#     plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()


#thresholding
# ret1, th1 = cv.threshold(enhance, 10, 255, cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(enhance,255,cv.ADAPTIVE_THRESH_MEAN_C,\
#             cv.THRESH_BINARY,11,2)

# th3 = cv.adaptiveThreshold(enhance,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,11,2)
# ret4, th4 = cv.threshold(enhance, 10, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


# titles = ['Pre-Processed Image', 'Global Thresholding (value = 10)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding', 'Otsu Thresholding']
# images = [enhance, th1, th2, th3, th4]
# for i in range(5):
#     plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

#snakes / deformable models / active contours






