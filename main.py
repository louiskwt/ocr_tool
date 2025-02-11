import os, csv
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_path) -> str:
    pages = convert_from_path(pdf_path)
    text = ""
    
    for i, page in enumerate(pages):
        tmp_image = f'page_{i}.jpg'
        page.save(tmp_image, 'JPEG')
        text += pytesseract.image_to_string(Image.open(tmp_image))
        os.remove(tmp_image)

    return text

def parse_and_format_words_from_extracted_text(text: str) -> list[str]:
    splited_words = [word.lower() for word in text.split() if len(word) > 2 and not word.isupper() and word.isalpha()]
    return list(dict.fromkeys(splited_words))

def save_words_into_csv(words: list[str], year: str) -> None:
    with open(f'{year}.csv', 'w') as f:
        header = ["Word", "pos", "year"]
        writer = csv.writer(f)
        writer.writerow(header)
        for w in words:
            writer.writerow([w, "", year])


pdf = "2012.pdf"
extracted_text = extract_text_from_pdf(pdf)
words = parse_and_format_words_from_extracted_text(extracted_text)
save_words_into_csv(words, "2012")
