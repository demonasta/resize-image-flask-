from PIL import Image
import os

def resize_image(input_path, output_folder, size):
    try:
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Open the image using Pillow (PIL)
        image = Image.open(input_path)

        # Get the original image dimensions
        original_width, original_height = image.size

        # Calculate the new dimensions while maintaining the aspect ratio
        if original_width > original_height:
            new_width = size
            new_height = int((original_height / original_width) * size)
        else:
            new_height = size
            new_width = int((original_width / original_height) * size)

        # Resize the image
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Save the resized image to the output folder
        output_path = os.path.join(output_folder, os.path.basename(input_path))
        resized_image.save(output_path)

        return output_path  # Return the path to the resized image

    except Exception as e:
        # Handle any errors, such as invalid image formats
        print(f"Error: {str(e)}")
        return None
