from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Load the image
input_image_path = "input_image.jpg"  # Replace with your image file path
output_image_path = "output_image.jpg"

# Open the input image
image = Image.open(input_image_path)

# Function to display images
def display_images(original, modified, title1="Original Image", title2="Modified Image"):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(original)
    axes[0].set_title(title1)
    axes[0].axis("off")
    axes[1].imshow(modified)
    axes[1].set_title(title2)
    axes[1].axis("off")
    plt.show()

# 1. Rotation
rotated_image = image.rotate(45, expand=True)  # Rotate by 45 degrees

# Display rotation
display_images(image, rotated_image, "Original Image", "Rotated Image")
rotated_image.save("rotated_image.jpg")

# 2. Scaling
scaled_image = image.resize((int(image.width * 1.5), int(image.height * 1.5)))  # Scale by 1.5x

# Display scaling
display_images(image, scaled_image, "Original Image", "Scaled Image")
scaled_image.save("scaled_image.jpg")

# 3. Translation
translation_offset = (50, 100)  # Translate by (x, y)
translated_image = ImageOps.expand(image, border=(translation_offset[0], translation_offset[1], 0, 0), fill="white")

# Display translation
display_images(image, translated_image, "Original Image", "Translated Image")
translated_image.save("translated_image.jpg")

# 4. Skewing
from PIL import ImageTransform
width, height = image.size
skew_transform = ImageTransform.AffineTransform(
    (1, 0.3, 0,  # x-axis skew
     0.3, 1, 0)  # y-axis skew
)
skewed_image = image.transform((width, height), Image.AFFINE, skew_transform.getdata())

# Display skewing
display_images(image, skewed_image, "Original Image", "Skewed Image")
skewed_image.save("skewed_image.jpg")
