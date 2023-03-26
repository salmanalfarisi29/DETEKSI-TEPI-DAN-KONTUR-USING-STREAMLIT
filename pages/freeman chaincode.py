import cv2
import numpy as np
import streamlit as st

def preprocess_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    return thresh_image

def find_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def find_freeman_chaincode(contour):
    chaincode = []
    x, y, w, h = cv2.boundingRect(contour)
    roi = np.zeros_like(image)
    cv2.drawContours(roi, [contour], -1, 255, -1)
    padded_roi = np.pad(roi, 1, mode='constant', constant_values=0)
    for point in contour:
        x, y = point[0]
        x += 1
        y += 1
        code = 0
        if padded_roi[y-1, x+1] == 255:
            code = 1
        elif padded_roi[y, x+1] == 255:
            code = 2
        elif padded_roi[y+1, x+1] == 255:
            code = 3
        elif padded_roi[y+1, x] == 255:
            code = 4
        elif padded_roi[y+1, x-1] == 255:
            code = 5
        elif padded_roi[y, x-1] == 255:
            code = 6
        elif padded_roi[y-1, x-1] == 255:
            code = 7
        elif padded_roi[y-1, x] == 255:
            code = 8
        chaincode.append(code)
    return chaincode

def calculate_chain_code(chaincode):
    if len(contours) == 1:
        contour = contours[0]
        chaincode = find_freeman_chaincode(contour)
        st.write('Chain code:', chaincode)
        digit = calculate_chain_code(chaincode)
        if digit is not None:
            st.write('Identified digit:', digit)
        else:
            st.warning('Failed to identify the digit')
    elif len(contours) > 1:
        st.warning('Multiple contours found')
    else:
        st.warning('No contours found')

    digit_map = {
        (1, 1, 1, 1, 1, 1, 1, 0): 0,
        (1, 1, 1, 1, 1, 1, 0, 1): 1,
        (1, 1, 1, 1, 1, 1, 0, 0): 2,
        (1, 1, 1, 1, 1, 0, 1, 1): 3,
        (1, 1, 1, 1, 1, 0, 1, 0): 4,
        (1, 1, 1, 1, 1, 0, 0, 1): 5,
        (1, 1, 1, 1, 1, 0, 0, 0): 6,
        (1, 1, 1, 1, 0, 1, 1, 1): 7,
        (1, 1, 1, 1, 0, 0, 1, 1): 8,
        (1, 1, 1, 1, 0, 0, 1, 0): 9

        # (4, 4, 4, 4, 4, 4, 4, 0): 0,
        # (4, 4, 4, 4, 4, 4, 0, 4): 1,
        # (4, 4, 4, 4, 4, 4, 0, 0): 2,
        # (4, 4, 4, 4, 4, 0, 4, 4): 3,
        # (4, 4, 4, 4, 4, 0, 4, 0): 4,
        # (4, 4, 4, 4, 4, 0, 0, 4): 5,
        # (4, 4, 4, 4, 4, 0, 0, 0): 6,
        # (4, 4, 4, 4, 0, 4, 4, 4): 7,
        # (4, 4, 4, 4, 0, 0, 4, 4): 8,
        # (4, 4, 4, 4, 0, 0, 4, 0): 9
    }
    for k, v in digit_map.items():
        if chaincode == k:
            return v
    return ""



# def identify_digit(gray):
#     # Apply Sobel operator to find edges
#     sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
#     sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
#     mag = np.sqrt(sobelx**2 + sobely**2)

#     # Threshold to create binary image
#     _, thresh = cv2.threshold(mag, 50, 255, cv2.THRESH_BINARY)

#     # Find contours in binary image
#     contours, _ = cv2.findContours(thresh.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Find contour with largest area
#     largest_contour = max(contours, key=cv2.contourArea)

#     # Calculate Freeman Chain Code
#     freeman_code = []
#     for i in range(1, len(largest_contour)):
#         diff = largest_contour[i] - largest_contour[i-1]
#         freeman_code.append(np.mod(np.angle(complex(*diff.squeeze())), 2*np.pi) / (np.pi/4))

#     # Match Freeman Chain Code with known patterns
#     if freeman_code == [1, 0, 0, 0, 0, 0, 0, 0, 1]:
#         return "Digit 0"
#     elif freeman_code == [0, 0, 0, 1, 1, 1, 0, 0, 0]:
#         return "Digit 1"
#     elif freeman_code == [0, 0, 0, 1, 1, 0, 0, 0, 1]:
#         return "Digit 2"
#     elif freeman_code == [0, 0, 1, 1, 0, 1, 0, 0]:
#         return "Digit 3"
#     elif freeman_code == [1, 0, 0, 1, 0, 1, 0, 1]:
#         return "Digit 4"
#     elif freeman_code == [1, 0, 0, 1, 1, 0, 0, 1]:
#         return "Digit 5"
#     elif freeman_code == [1, 0, 1, 0, 1, 1, 0, 1]:
#         return "Digit 6"
#     elif freeman_code == [0, 0, 0, 1, 0, 0, 0, 1]:
#         return "Digit 7"
#     elif freeman_code == [1, 0, 1, 0, 1, 0, 0, 1]:
#         return "Digit 8"
#     elif freeman_code == [0, 1, 0, 1, 0, 0, 1, 0]:
#         return "Digit 9"
#     else:
#         return "Tidak dikenali"

# Streamlit app to get Freeman Chain Code from image using Sobel method
st.title("Freeman Chain Code using Sobel Method")
st.write("Upload an image containing a single digit (0-9) with white background")

# file upload
uploaded_file = st.file_uploader("Pilih gambar")

if uploaded_file is not None:
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    st.image(img, caption='Gambar Asli', use_column_width=True)
    preprocessed_image = preprocess_image(img)
    st.image(preprocessed_image, caption='Gambar Gray', use_column_width=True)
    contours = find_contours(preprocessed_image)
    st.write('Number of contours found:', len(contours))


    for contour in contours:
        chain_code = calculate_chain_code(contour)
        st.write('Chain code:', chain_code)


    # # read the image using OpenCV
    # img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # display the image
    # st.image(img, caption="Gambar asli", use_column_width=True)

    # st.image(gray, caption="Gambar Gray", use_column_width=True)

    # # get the Freeman Chain Code using Sobel method
    # chain_code = identify_digit(gray)

    # # display the chain code
    # st.write("Freeman Chain Code: ", chain_code)