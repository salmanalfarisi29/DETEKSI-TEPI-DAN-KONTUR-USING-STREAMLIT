import streamlit as st
import numpy as np
import cv2
from colormath.color_objects import XYZColor, LabColor
from colormath.color_conversions import convert_color

# Tampilan Streamlit
st.title("Konversi warna XYZ")

st.text("___________________________________________________________________________________________________________________________")
#XYZ KE RGB
st.title("Konversi XYZ ke RGB")
def XYZ2RGB(XYZ):
    # Definisikan matriks transformasi XYZ ke RGB
    M = np.array([[0.41847, -0.15866, -0.082835],
                  [-0.091169, 0.25243, 0.015708],
                  [0.00092090, 0.0025498, 0.17860]])

    # melakukan perkalian matriks antara nilai XYZ dengan matriks transformasi M yang telah ditransposisi (M.T) menggunakan fungsi dot dari NumPy dan disimpan ke dalam variabel RGB
    RGB = np.dot(XYZ, M.T)

    # Batasi nilai RGB ke rentang [0, 1]
    # agar nilai RGB tidak melebihi batas maksimum (255) dan batas minimum (0)
    RGB[RGB < 0] = 0
    RGB[RGB > 1] = 1

    # Konversi nilai RGB ke rentang [0, 255]
    RGB = np.uint8(RGB * 255)

    return RGB

# Menambahkan input untuk memilih citra
uploaded_file = st.file_uploader("Pilih citra dalam format PNG atau JPG", type=["png", "jpg"])

# Memuat citra jika ada
if uploaded_file is not None:
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

    # Konversi citra dari XYZ ke RGB
    rgb_img = XYZ2RGB(img)

    # Menampilkan citra asli dan hasil konversi di Streamlit
    st.text("Hasil Konversi")
    st.image(np.hstack([cv2.cvtColor(img, cv2.COLOR_XYZ2BGR), rgb_img]))
    st.text("Diperbesar")
    st.image(np.hstack([cv2.cvtColor(img, cv2.COLOR_XYZ2BGR), rgb_img]), width=80)

else:
    st.warning("Silakan pilih citra terlebih dahulu")

st.text("___________________________________________________________________________________________________________________________")

#XYZ KE HSV

def rgb_to_xyz(rgb_img):
    # Convert RGB image to XYZ
    xyz_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2XYZ)
    return xyz_img

def xyz_to_hsv(xyz_img):
    # Convert XYZ image to RGB
    rgb_img = cv2.cvtColor(xyz_img, cv2.COLOR_XYZ2RGB)
    # Convert RGB image to HSV
    hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)
    return hsv_img

def main():
    st.title("Konversi XYZ ke HSV")
    uploaded_file = st.file_uploader("Upload gambar dalam format JPG atau PNG", type=["jpg", "png"])
    if uploaded_file is not None:
        # Baca gambar
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        # Konversi citra ke format XYZ
        xyz_img = rgb_to_xyz(img)
        # Konversi citra ke format HSV
        hsv_img = xyz_to_hsv(xyz_img)
        # Tampilkan citra dalam format HSV
        st.text("Hasil Konversi")
        st.image(hsv_img)
        st.text("Diperbesar")
        st.image(hsv_img, width = 80)
if __name__ == "__main__":
    main()
    
st.text("___________________________________________________________________________________________________________________________")  

#XYZ KE CMY

def rgb_to_xyz(rgb_img):
    # Convert RGB image to XYZ
    xyz_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2XYZ)
    return xyz_img

def xyz_to_cmy(xyz_img):
    # Convert XYZ image to CMY
    cmy_img = 1 - xyz_img / 255
    return cmy_img

def main():
    st.title("Konversi XYZ ke CMY")
    uploaded_file = st.file_uploader("Upload gambar dalam format JPG atau PNG", key="uploader", type=["jpg", "png"])
    if uploaded_file is not None:
        # Baca gambar
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        # Konversi citra ke format XYZ
        xyz_img = rgb_to_xyz(img)
        # Konversi citra ke format CMY
        cmy_img = xyz_to_cmy(xyz_img)
        # Tampilkan citra dalam format CMY
        st.text("Hasil Konversi")
        st.image(cmy_img)
        st.text("Diperbesar")
        st.image(cmy_img, width=80)

if __name__ == "__main__":
    main()
    
st.text("___________________________________________________________________________________________________________________________")

#XYZ KE CIELab

def rgb_to_xyz(rgb_img):
    # Convert RGB image to XYZ
    xyz_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2XYZ)
    return xyz_img

def xyz_to_lab(xyz_img):
    # Convert XYZ image to CIELab
    lab_img = np.zeros_like(xyz_img)
    for i in range(xyz_img.shape[0]):
        for j in range(xyz_img.shape[1]):
            # Convert XYZ color to Lab color
            xyz_color = XYZColor(xyz_img[i, j, 0], xyz_img[i, j, 1], xyz_img[i, j, 2])
            lab_color = convert_color(xyz_color, LabColor)
            # Set Lab color to output image
            lab_img[i, j, 0] = lab_color.lab_l
            lab_img[i, j, 1] = lab_color.lab_a
            lab_img[i, j, 2] = lab_color.lab_b
    return lab_img

def main():
    st.title("Konversi XYZ ke CIELab")
    uploaded_file = st.file_uploader("Upload gambar dalam format JPG atau PNG", key="uploader2CIELab", type=["jpg", "png"])
    if uploaded_file is not None:
        # Baca gambar
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        # Konversi citra ke format XYZ
        xyz_img = rgb_to_xyz(img)
        # Konversi citra ke format CIELab
        lab_img = xyz_to_lab(xyz_img)
        # Tampilkan citra dalam format CIELab
        st.image(lab_img, width=80)

if __name__ == "__main__":
    main()