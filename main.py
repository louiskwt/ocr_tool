import os, csv, pytesseract, spacy
from pdf2image import convert_from_path
from PIL import Image
from tqdm import tqdm
from utils import remove_duplicates_by_property, validate_word

def extract_words_from_pdf(pdf_path: str, source: str) -> list[list[dict]]:
    pages = convert_from_path(pdf_path)
    text = []
    pbar = tqdm(enumerate(pages))
    for i, page in pbar: 
        pbar.set_description(f"Processing page no. {i+1}")
        tmp_image = f'page_{i}.jpg'
        page.save(tmp_image, 'JPEG')
        img_string = pytesseract.image_to_string(Image.open(tmp_image))
        words = parse_and_format_words_from_extracted_text(img_string)
        formated_words = [{"word": w[0], "pos": w[1], "source": source, "page": i + 1} for w in words]
        text.append(formated_words)
        os.remove(tmp_image)
    return text

def parse_and_format_words_from_extracted_text(text: str) -> list[tuple]:
    splited_words = [word.lower() for word in text.split() if validate_word(word)]
    cleaned_words = list(dict.fromkeys(splited_words))
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(" ".join(cleaned_words))
    return [(token.text, token.pos_) for token in doc]

def save_words_into_csv(word_pages: list[dict], source: str) -> None:
    keys = word_pages[0].keys()
    with open(f'{source}.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(word_pages)


pdf = "2018R.pdf"
word_pages = extract_words_from_pdf(pdf, source=pdf.split(".")[0])
flattend_word_pages = [d for page in word_pages for d in page]
cleaned_word_pages = remove_duplicates_by_property(flattend_word_pages, "word")
save_words_into_csv(cleaned_word_pages, pdf.split(".")[0])
