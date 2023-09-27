from PIL import Image, ImageDraw, ImageFont
from ocr import OCR
import textwrap
import argparse

parser = argparse.ArgumentParser(description="Handwriting image manipulation")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

class HandWriting:

    def __init__(self, image_path):

        self.image_path = image_path


    def generate_img(self):

        input_image_path = "images/input.png"
        image = Image.open(input_image_path)
        draw = ImageDraw.Draw(image)
        ocr = OCR(self.image_path)
        text = ocr.extract_text()

        font_path = "fonts/Coal-Hand-Luke.ttf"
        font_size = 40  # Adjust the font size as needed

        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            font = ImageFont.load_default()
            font_size = 200  # Use a default font and size if the OTF font cannot be loaded

        # Specify the position where you want to start placing the text
        text_position = (50, 50)  # (x, y) coordinates

        # Define the color of the text (black)
        text_color = (0, 0, 0)  # Black color

        # Define the maximum width for each line of text

        # Wrap the text to fit within the specified width
        wrapped_text = textwrap.fill(text, width=70)  # Adjust the width as needed

        # Split the wrapped text into lines
        lines = wrapped_text.split('\n')

        current_position = text_position

        # Add each line of text to the image
        for line in lines:
            draw.text(current_position, line, fill=text_color, font=font)
            # Move the position down by the height of the current line
            current_position = (text_position[0], current_position[1] + font_size)

        # Save the modified image
        output_image_path = "images/output/output_image.png"
        image.save(output_image_path)

        # Display the image (optional)
        image.show()

        # Close the image
        image.close()


if __name__ == "__main__":

    ocr = HandWriting(args.image)
    ocr.generate_img()