import os
from PIL import Image

def batch_resize_images(input_folder, output_folder, target_width, target_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        try:
            with Image.open(input_path) as img:
                resized_img = img.resize((target_width, target_height), Image.LANCZOS)
                resized_img.save(output_path)
                print(f"Resized and saved {filename}")
        except Exception as e:
            print(f"Skipping {filename}: {e}")


input_folder = "D:\\Irys_Spritetype-1.1\\New folder"
output_folder = "D:\\Irys_Spritetype-1.1\\New folder"

target_width = 800
target_height = 600

batch_resize_images(input_folder, output_folder, target_width, target_height)