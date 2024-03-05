from PIL import Image
import os

def resize_images(input_dir, output_dir, width, height):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image file
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)

            # Resize the image using Lanczos resampling
            resized_image = image.resize((width, height), resample=Image.LANCZOS)

            # Save the resized image to the output directory
            output_path = os.path.join(output_dir, filename)
            resized_image.save(output_path)

            print(f"Resized {filename} successfully.")

# Specify the input directory, output directory, and target dimensions
input_dir = "C:/Users/moham/Desktop/Test nonfaces 1"
output_dir = "C:/Users/moham/Desktop/Scaled nonfaces 1"
width = 92
height = 112

# Call the resize_images function
resize_images(input_dir, output_dir, width, height)