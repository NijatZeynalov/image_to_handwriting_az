# Azerbaijani Text to Handwriting Converter

The Azerbaijani Text to Handwriting Converter is a versatile Python application that seamlessly transforms digital text into elegant Azerbaijani handwriting. This project employs Optical Character Recognition (OCR) for text recognition and subsequently generates visually appealing images of the text, emulating the artistry of handwritten Azerbaijani script.


## Table of Contents

- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Usage](#Usage)
- [License](#license)

---

## Prerequisites

To install the necessary Python packages, execute the following command:

```python
pip install -r requirements.txt
```

## Installation

Begin by cloning this repository to your local environment:

```python
git clone https://github.com/NijatZeynalov/text-to-handwriting-az.git
```

Navigate to the project directory:

```python
cd text-to-handwriting-az
```

# Usage
To convert text to Azerbaijani handwriting, follow these steps:

Run the project with the following command, providing the text you wish to convert and specifying the output image file:

```python
python src/text_to_handwriting.py --image 'images/tests/test_1.png'
```

The application will commence by conducting OCR on the input image, followed by the generation of a captivating image featuring the handwritten Azerbaijani script. The resulting image will be stored at the designated output location.

## Examples:

Test image:

![input_image](https://github.com/NijatZeynalov/mgpt-az-streamlit/assets/31247506/7e4d056a-6165-47a9-bc7e-2fbe9cee6662)

Result:

![output_image](https://github.com/NijatZeynalov/mgpt-az-streamlit/assets/31247506/5031f4d7-309b-4cf1-9ed1-1f80453785b8)


## Contributing
I welcome contributions to this project from the community. Please don't hesitate to open issues or submit pull requests to enhance functionality or introduce new features. Together, we can improve this project and make it even more valuable.

## License
This project is licensed under the MIT License. Feel free to adapt and use it as needed within the boundaries of this license.
