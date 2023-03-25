import cv2
import numpy as np
import streamlit as st

# function to get Freeman chain code from contour using Sobel method
def get_freeman_chain_code_sobel(img):
    # convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply Sobel filter to get the edges
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edges = cv2.Canny(sobelx, sobely, 50, 150)

    # get the contour
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # get the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # get the Freeman Chain Code for the largest contour
    chain_code = get_freeman_chain_code_sobel(largest_contour)

    return chain_code

# Streamlit app to get Freeman Chain Code from image using Sobel method
st.title("Freeman Chain Code using Sobel Method")
st.write("Upload an image containing a single digit (0-9) with white background")

# file upload
uploaded_file = st.file_uploader("Pilih gambar")

if uploaded_file is not None:
    # read the image using OpenCV
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

    # display the image
    st.image(img, caption="Gambar asli", use_column_width=True)

    # get the Freeman Chain Code using Sobel method
    chain_code = get_freeman_chain_code_sobel(img)

    # display the chain code
    st.write("Freeman Chain Code: ", chain_code)
