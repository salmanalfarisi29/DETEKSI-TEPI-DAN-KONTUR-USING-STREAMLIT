import streamlit as st
from PIL import Image
import cv2
import numpy as np
import copy

# def onlyOne(color):
#     pil = Image.fromarray(color)
#     return pil

# def oneChannel(var):
#     merged = cv2.merge(var)
#     pil = Image.fromarray(merged)
#     return pil


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

def main():
    st.title("DETEKSI TEPI")
    with st.container():
        # task 0
        st.header('SILAHKAN UPLOAD GAMBAR ANDA')
        img = st.file_uploader("Pilih gambar",['png','jpg','jpeg'])
        if img is not None:
            st.image(img)
            img = convertImage(img)
            r, g, b = cv2.split(img)
            
            r_dup = copy.deepcopy(r)
            g_dup = copy.deepcopy(g)
            b_dup = copy.deepcopy(b)

            r_dup[:] = 0
            g_dup[:] = 0
            b_dup[:] = 0

if __name__ == '__main__':
	main()