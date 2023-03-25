import cv2
import numpy as np
import streamlit as st

def identify_digit(gray):
    # Apply Sobel operator to find edges
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    mag = np.sqrt(sobelx**2 + sobely**2)

    # Threshold to create binary image
    _, thresh = cv2.threshold(mag, 50, 255, cv2.THRESH_BINARY)

    # Find contours in binary image
    contours, _ = cv2.findContours(thresh.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find contour with largest area
    largest_contour = max(contours, key=cv2.contourArea)

    # Calculate Freeman Chain Code
    freeman_code = []
    for i in range(1, len(largest_contour)):
        diff = largest_contour[i] - largest_contour[i-1]
        freeman_code.append(np.mod(np.angle(complex(*diff.squeeze())), 2*np.pi) / (np.pi/4))

    # Match Freeman Chain Code with known patterns
    if freeman_code == [1, 0, 0, 0, 0, 0, 0, 1]:
        return "Digit 0"
    elif freeman_code == [0, 0, 0, 1, 1, 1, 0, 0]:
        return "Digit 1"
    elif freeman_code == [0, 0, 1, 1, 0, 0, 0, 1]:
        return "Digit 2"
    elif freeman_code == [0, 0, 1, 1, 0, 1, 0, 0]:
        return "Digit 3"
    elif freeman_code == [1, 0, 0, 1, 0, 1, 0, 1]:
        return "Digit 4"
    elif freeman_code == [1, 0, 0, 1, 1, 0, 0, 1]:
        return "Digit 5"
    elif freeman_code == [1, 0, 1, 0, 1, 1, 0, 1]:
        return "Digit 6"
    elif freeman_code == [0, 0, 0, 1, 0, 0, 0, 1]:
        return "Digit 7"
    elif freeman_code == [1, 0, 1, 0, 1, 0, 0, 1]:
        return "Digit 8"
    elif freeman_code == [0, 1, 0, 1, 0, 0, 1, 0]:
        return "Digit 9"
    else:
        return "Tidak dikenali"

# Streamlit app to get Freeman Chain Code from image using Sobel method
st.title("Freeman Chain Code using Sobel Method")
st.write("Upload an image containing a single digit (0-9) with white background")

# file upload
uploaded_file = st.file_uploader("Pilih gambar")

if uploaded_file is not None:
    # read the image using OpenCV
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # display the image
    st.image(img, caption="Gambar asli", use_column_width=True)

    st.image(gray, caption="Gambar Gray", use_column_width=True)

    # get the Freeman Chain Code using Sobel method
    chain_code = identify_digit(gray)

    # display the chain code
    st.write("Freeman Chain Code: ", chain_code)