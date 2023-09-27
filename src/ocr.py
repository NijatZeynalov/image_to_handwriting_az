import easyocr


class OCR:

    def __init__(self, image_path):
        self.image_path = image_path

    def extract_text(self):

        # Create an EasyOCR object
        reader = easyocr.Reader(["az"])

        # Detect and recognize the text in the image
        results = reader.readtext(self.image_path)

        result_text = []
        for result in results:
            result_text.append(result[1])

        return ' '.join(result_text)
    #
