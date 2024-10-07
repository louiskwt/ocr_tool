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
