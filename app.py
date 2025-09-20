import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Hackathon CV Starter App 🖼️")

st.write("Upload an image and apply basic Computer Vision filters using OpenCV.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to OpenCV format
    img_array = np.array(image)
    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Choose operation
    option = st.selectbox(
        "Choose a filter",
        ("Grayscale", "Canny Edge Detection", "Blur"),
    )

    if option == "Grayscale":
        result = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        st.image(result, caption="Grayscale Image", use_column_width=True, channels="GRAY")

    elif option == "Canny Edge Detection":
        result = cv2.Canny(img_cv, 100, 200)
        st.image(result, caption="Edges Detected", use_column_width=True, channels="GRAY")

    elif option == "Blur":
        result = cv2.GaussianBlur(img_cv, (15, 15), 0)
        st.image(result, caption="Blurred Image", use_column_width=True)
