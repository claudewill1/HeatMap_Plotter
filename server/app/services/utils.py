import base64

def convert_image_to_base64(image_path: str) -> str:
    """
    Convert an image file to a base64 string.
    -Open image in binary mode.
    - Read contents.
    - Encode to base64 string.
    - Return base64 string.
    """
    try:
        # Open image file in binary mode
        with open(image_path, "rb") as image_file:
            # Read the contents of the image file
            image_data = image_file.read()
            # Encode the image data to base64
            base64_string = base64.b64encode(image_data).decode('utf-8')
            return base64_string
    except Exception as e:
        # Handle exceptions (e.g., file not found, read errors)
        raise Exception(f"Error converting image to base64: {str(e)}")
    