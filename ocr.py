from PIL import Image
import pytesseract
import cv2
import os
import re


def get_initial_dir():
    """
    Returns the current working directory.
    """
    return os.getcwd().replace('"', '')


def img_to_text(filepath):
    """
Converts an image file to text using Tesseract OCR.

Args:
    filepath (str): The path to the image file.

Returns:
    str: The text extracted from the image.
    """
    try:
        # Check if file is an image
        file_extension = os.path.splitext(filepath)[1]
        if file_extension.lower() not in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
            return None
        # Load image and convert to grayscale
        image = cv2.imread(filepath)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        filename = f"{os.getpid()}.png"
        cv2.imwrite(filename, image)

        # Extract text from image
        with Image.open(filename) as img:
            text = pytesseract.image_to_string(img)
            text = re.sub(r'\n\s*\n', '\n', text)
            # print(repr(text))
        # Delete temporary image file
        os.remove(filename)

        return text

    except FileNotFoundError:
        # print(f"Error: File {filepath} not found.")
        return None

    except Exception as e:
        # print(f"Error: {e}")
        return None
