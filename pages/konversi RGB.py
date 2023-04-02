import streamlit as st
import numpy as np
import cv2
from colormath.color_objects import XYZColor, LabColor
from colormath.color_conversions import convert_color

# Tampilan Streamlit
st.title("Konversi warna RGB")

st.text("___________________________________________________________________________________________________________________________")
def rgb2hsv(rgb):
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv

# Fungsi untuk memperbesar gambar
def resize_image(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# Judul halaman
st.title("Konversi Citra RGB ke HSV")

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Baca gambar menggunakan OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Konversi gambar dari format RGB ke format HSV
    img_hsv = rgb2hsv(image)

    # Perbesar gambar
    img_hsv = resize_image(img_hsv, 3)

    # Tampilkan gambar
    st.text("Hasil Konversi")
    st.image(img_hsv, channels="HSV")
    st.text("Diperbesar")
    st.image(img_hsv, channels="HSV", width=800)
st.text("___________________________________________________________________________________________________________________________")
def rgb2xyz(rgb):
    xyz = cv2.cvtColor(rgb, cv2.COLOR_RGB2XYZ)
    return xyz

# Fungsi untuk memperbesar gambar
def resize_image(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# Judul halaman
st.title("Konversi Citra RGB ke XYZ")

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"], key="uploader")

if uploaded_file is not None:
    # Baca gambar menggunakan OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Konversi gambar dari format RGB ke format XYZ
    img_xyz = rgb2xyz(image)

    # Perbesar gambar
    img_xyz = resize_image(img_xyz, 3)

    # Tampilkan gambar
    st.text("Hasil Konversi")
    st.image(img_xyz, channels="RGB")
    st.text("Diperbesar")
    st.image(img_xyz, channels="HSV", width=800)
    