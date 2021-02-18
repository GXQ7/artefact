import streamlit  as st
import io
import cv2 as cv
import supervised_segmentation as ss
import numpy as np 
import PIL.Image as Image


st.title("Web-based Image Segmentation Tool")
uploaded_file_objs = st.file_uploader("", type=["jpg","png"], accept_multiple_files=True, key="uploader")

#The UploadedFile class is a subclass of BytesIO, and therefore it is “file-like”. 
# This means you can pass them anywhere where a file is expected.
# >>> None or Uploaded File

if uploaded_file_objs is not None:
    print("not none")

# img = st.image("GlaucomaImages\\001.jpg", use_column_width=True, key="uploader")

"""Pre-processing Techniques"""
grey = st.button("Convert to Grey Scale", key='grey')
if grey: 
    img = cv.imread("GlaucomaImages\\001.jpg", 1)
    ss.convert_greyscale(img) #error - expecting <cv::Umat>
    
    st.image(img, use_column_width=True)



smooth = st.button("Smooth image", key='smooth')
enhance = st.button("Enhance image", key='enchance')


"""Segmentation Techniques"""
othresh = st.button("Adaptive Thresholding", key='athresh')
snakes = st.button("Active Contours", key='snakes')
rwalker = st.button("Random Walker", key='rwalker')



# user can then apply segmentation techniques using (menu or buttons)