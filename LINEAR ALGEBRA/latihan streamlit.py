import os
from PIL import Image, ImageOps
import streamlit as st
from io import BytesIO

# Fungsi untuk menampilkan gambar
def display_image_with_title(image, title):
    st.subheader(title)
    st.image(image, use_column_width=True)

# Fungsi untuk melakukan skew
def skew_image(image, skew_x=0.5, skew_y=0):
    width, height = image.size
    x_shift = skew_x * height
    new_width = width + abs(x_shift)
    skew_matrix = (1, skew_x, -x_shift if x_shift > 0 else 0, skew_y, 1, 0)
    return image.transform((int(new_width), height), Image.AFFINE, skew_matrix)

# Judul aplikasi
st.title("Image Transformation App")
st.write("Upload an image and apply transformations like rotation, scaling, translation, and skewing.")

# Upload file gambar
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Buka gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Rotasi
    angle = st.slider("Rotate Image (degrees):", min_value=0, max_value=360, value=45)
    rotated_image = image.rotate(angle, expand=True)
    display_image_with_title(rotated_image, "Rotated Image")

    # Scaling
    scale_factor = st.slider("Scale Image (factor):", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
    scaled_image = image.resize((int(image.width * scale_factor), int(image.height * scale_factor)))
    display_image_with_title(scaled_image, "Scaled Image")

    # Translasi
    translate_x = st.slider("Translate Image (X-axis, pixels):", min_value=0, max_value=200, value=50)
    translate_y = st.slider("Translate Image (Y-axis, pixels):", min_value=0, max_value=200, value=50)
    translated_image = ImageOps.expand(image, border=(translate_x, translate_y, 0, 0), fill="white")
    display_image_with_title(translated_image, "Translated Image")

    # Skewing
    skew_x = st.slider("Skew Image (X-axis factor):", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    skewed_image = skew_image(image, skew_x=skew_x)
    display_image_with_title(skewed_image, "Skewed Image")

    # Download tombol untuk setiap transformasi
    st.subheader("Download Transformed Images")
    for transformed_image, title in zip(
        [rotated_image, scaled_image, translated_image, skewed_image],
        ["Rotated", "Scaled", "Translated", "Skewed"]
    ):
        buf = BytesIO()
        transformed_image.save(buf, format="JPEG")
        byte_data = buf.getvalue()
        st.download_button(
            label=f"Download {title} Image",
            data=byte_data,
            file_name=f"{title.lower()}_image.jpg",
            mime="image/jpeg"
        )

st.write("Developed with ❤️ using Streamlit.")
