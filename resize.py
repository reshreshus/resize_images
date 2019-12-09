"""
Get images, resize and save)
"""

from PIL import Image
import os

input_folder = 'input'
output_folder = 'output'
OUTPUT_SIZE = (256, 256)


for image_name in os.listdir(input_folder):
    img = Image.open(os.path.join(input_folder, image_name))
    # I downsize the image with an ANTIALIAS filter (gives the highest quality)
    img = img.resize(OUTPUT_SIZE, Image.ANTIALIAS)
    img.save(os.path.join(output_folder, image_name), optimize=True,quality=95)


