<<<<<<< HEAD
import pathlib

from pdf2image import convert_from_path


# Converting pdf to img first
def convert_pdf_to_img(path):
    CURRENT_DIR = pathlib.Path(__file__).parent.absolute()
    pdfs = CURRENT_DIR / "test_files" / path
    pages = convert_from_path(pdfs, 500)
    num_of_pages = len(pages)
    for i in range(num_of_pages):
        img_name = f"test{i + 1}.jpg"
        pages[i].save(img_name, "JPEG")

def main():
    convert_pdf_to_img("test.pdf")


if __name__ == "__main__":
    main()

import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    
    for i, page in enumerate(pages):
        tmp_image = f'page_{i}.jpg'
        page.save(tmp_image, 'JPEG')
        text += pytesseract.image_to_string(Image.open(tmp_image))
        os.remove(tmp_image)

    return text

pdf = "test2.pdf"
extracted_text = extract_text_from_pdf(pdf)
print(extracted_text)