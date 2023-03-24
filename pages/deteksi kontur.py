import cv2
import numpy as np
import streamlit as st

# Fungsi untuk menghitung operator Sobel pada gambar
def sobel_operator(image):
    # Apply Sobel operator in X and Y direction
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

    # Convert the gradient images to 8-bit unsigned integers
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)

    # Combine the gradient images using bitwise OR
    sobel_combined = cv2.bitwise_or(sobelx, sobely)
    return sobel_combined

# Tampilan Streamlit
st.title("Deteksi Kontur dengan Operator Sobel")

# Menu sidebar untuk memilih gambar
uploaded_file = st.file_uploader("Pilih gambar")

# Tampilan utama
if uploaded_file is not None:
    # Baca gambar dari file yang diunggah
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    
    # Tampilkan gambar asli
    st.image(image, caption="Gambar asli", use_column_width=True)
    
    # Hitung operator Sobel pada gambar asli
    sobel_combined = sobel_operator(image)
    
    # Tampilkan hasil operator Sobel
    st.image(sobel_combined, caption="Hasil operator Sobel", use_column_width=True)
else:
    st.empty()