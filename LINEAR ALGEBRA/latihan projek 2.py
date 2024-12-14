from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import os

input_image_path = r"C:\Users\ACER-USER\LINEAR ALGEBRA\jerome.jpeg.jpeg"
output_dir = "./output_images/"  # Output directory

if not os.path.exists(input_image_path):
    print(f"File tidak ditemukan di path: {input_image_path}")
else:
    image = Image.open(input_image_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def display_images(images, titles):
        fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
        for ax, img, title in zip(axes, images, titles):
            ax.imshow(img)
            ax.set_title(title)
            ax.axis("off")
        plt.tight_layout()
        plt.show()

    # 1. Rotasi
    rotated_image = image.rotate(45, expand=True)
    rotated_image.save(os.path.join(output_dir, "rotated_image.jpg"))

    # 2. Scaling
    scaled_image = image.resize((int(image.width * 2), int(image.height * 2)))
    scaled_image.save(os.path.join(output_dir, "scaled_image.jpg"))

    # 3. Translasi (Pergeseran)
    translated_image = ImageOps.expand(image, border=(50, 50, 0, 0), fill="white")
    translated_image.save(os.path.join(output_dir, "translated_image.jpg"))

    # 4. Skewing (Miring)
    def skew_image(image, skew_x=0.5, skew_y=0):
        width, height = image.size
        x_shift = skew_x * height
        new_width = width + abs(x_shift)
        skew_matrix = (1, skew_x, -x_shift if x_shift > 0 else 0, skew_y, 1, 0)
        return image.transform((int(new_width), height), Image.AFFINE, skew_matrix)

    skewed_image = skew_image(image, skew_x=0.5)
    skewed_image.save(os.path.join(output_dir, "skewed_image.jpg"))

    # Result
    images_to_display = [image, rotated_image, scaled_image, translated_image, skewed_image]
    titles = ["Original", "Rotated", "Scaled", "Translated", "Skewed"]
    display_images(images_to_display, titles)

    print("Transformasi selesai! Hasil disimpan di folder:", output_dir)