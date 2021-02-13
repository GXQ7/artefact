import preprocessing as pp
import cv2 as cv
import supervised_segmentation as ss
import matplotlib.pyplot as plt

rgb_test = pp.load_coloured_img("GlaucomaImages/001.jpg")
grey_test = pp.convert_greyscale(rgb_test)


#pre_processing
img = cv.imread("GlaucomaImages/001.jpg")
g = pp.get_green_channel(img)
img = pp.enhance_image(g)
blur = cv.medianBlur(img, 5)
resized = ss.resize_image(blur, 30)
cv.imshow('blurred', resized)
cv.waitKey(0)

# #thresholding
# ret1, th1 = cv.threshold(blur, 10, 255, cv.THRESH_BINARY)
# ret12, th2 = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, )

# ret1, th1 = cv.threshold(blur, 10, 255, cv.THRESH_BINARY)
# ret1, th1 = cv.threshold(blur, 10, 255, cv.THRESH_BINARY)

# ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
#             cv.THRESH_BINARY,11,2)
# th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,11,2)
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()







