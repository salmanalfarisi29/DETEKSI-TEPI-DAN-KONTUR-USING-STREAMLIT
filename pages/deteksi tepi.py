import streamlit as st
from PIL import Image
import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt

# def onlyOne(color):
#     pil = Image.fromarray(color)
#     return pil

# def oneChannel(var):
#     merged = cv2.merge(var)
#     pil = Image.fromarray(merged)
#     return pil

# Fungsi untuk menghitung operator Sobel dan menggabungkan hasilnya
def sobel_operator(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    return sobel

# Fungsi untuk melakukan normalisasi nilai pixel pada gambar
def normalize_image(img):
    img_min = np.min(img)
    img_max = np.max(img)
    return (img - img_min) / (img_max - img_min)

def convertImage(img):
    nparr = np.fromstring(img.getvalue(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# def ChangeColor(img):
#     img[np.where((img == [255, 0, 0]).all(axis=2))] = [255,255,0]
#     img[np.where((img == [0, 255, 0]).all(axis=2))] = [0,255,255]
#     img[np.where((img == [0, 0, 255]).all(axis=2))] = [255,0,255]
#     return img

# def main():
    # st.title("DETEKSI TEPI")
    # with st.container():
    #     # task 0
    #     st.header('SILAHKAN UPLOAD GAMBAR ANDA')
    #     img = st.file_uploader("Pilih gambar",['png','jpg','jpeg'])
    #     if img is not None:
    #         st.image(img)
    #         img = convertImage(img)
    #         r, g, b = cv2.split(img)
            
    #         r_dup = copy.deepcopy(r)
    #         g_dup = copy.deepcopy(g)
    #         b_dup = copy.deepcopy(b)

    #         r_dup[:] = 0
    #         g_dup[:] = 0
    #         b_dup[:] = 0

    #         st.image(img)
    #         img = convertImage(img)
    #         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #         plt.imshow(img, cmap='gray')
    #         plt.show()
            
    #         #Menerapkan filter sobel
    #         filter_sobel = cv2.Sobel(src=img, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=5)
            
    #         plt.imshow(filter_sobel, cmap='gray')
    #         plt.show()

# Halaman web Streamlit
def main():
    # Judul halaman
    st.title("Deteksi Tepi dengan Operator Sobel")

    # Pilihan upload gambar
    uploaded_file = st.file_uploader("Upload Gambar", type=["jpg", "jpeg", "png"])

    # Jika gambar telah diunggah
    if uploaded_file is not None:
        # Baca gambar
        image = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

        # Tampilkan gambar asli
        st.subheader("Gambar Asli")
        st.image(normalize_image(img), use_column_width=True)

        # Hitung operator Sobel dan tampilkan hasilnya
        sobel = sobel_operator(img)
        st.subheader("Hasil Deteksi Tepi")
        st.image(normalize_image(sobel), use_column_width=True)

if __name__ == '__main__':
	main()