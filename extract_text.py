import os, pytesseract 
from pdf2image import convert_from_path
from PIL import Image
from tqdm import tqdm
from utils import validate_word

def extract_text_from_pdf(pdf_path: str) -> list[str]:
    pages = convert_from_path(pdf_path)
    extracted_text = []
    pbar = tqdm(enumerate(pages))
    for i, page in pbar:
        pbar.set_description(f"Extracting page no. {i+1} / {len(pages)}")
        tmp_image = f'page_{i}.jpg'
        page.save(tmp_image, 'JPEG')
        img_string = pytesseract.image_to_string(Image.open(tmp_image), "eng")
        cleaned_img_string = " ".join([word for word in img_string.split() if validate_word(word)])
        extracted_text.append(cleaned_img_string)
        os.remove(tmp_image)
    return extracted_text

def save_text_into_txt(text_pages: list[str], source: str) -> None:
    with open(f'{source}.txt', 'w') as f:
        for page in text_pages:
            f.write(page)
            f.write("\n")

if __name__ == "__main__":
    print("Text extraction started...")
    pdf = "2018R.pdf"
    text = extract_text_from_pdf(pdf)
    save_text_into_txt(text, pdf.split(".")[0])