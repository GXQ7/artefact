import streamlit  as st
import io
import cv2 
import supervised_seg as ss
import numpy as np 



st.title("Web-based Image Segmentation Tool")

uploaded_file = st.file_uploader("", type=["jpg","png"])

#The UploadedFile class is a subclass of BytesIO, and therefore it is “file-like”. 
# This means you can pass them anywhere where a file is expected.
# >>> None or Uploaded File

if uploaded_file is not None:
    bytes_data = uploaded_file.read()  #returns byte contents of file
    st.image(bytes_data, use_column_width=True)



# user will be able to apply pre-procesing technqiues using a (menu or buttons)

"""Pre-processing Techniques"""
smooth = st.button("Smooth image", key='smooth')
enhance = st.button("Enhance image", key='enchance')


"""Segmentation Techniques"""
othresh = st.button("Otsu's Thresholding", key='othresh')
snakes = st.button("Active Contours", key='snakes')
rwalker = st.button("Random Walker", key='rwalker')



# user can then apply segmentation techniques using (menu or buttons)