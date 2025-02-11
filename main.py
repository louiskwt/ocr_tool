import os, csv
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

stopwords = [
    "a", "an", "the", "and", "or", "but", "if", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
    "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then", "once",
    "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
    "same", "so", "than", "too", "very",
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
    "themselves", "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "will", "would", "shall", "should",
    "can", "could", "may", "might", "must", "ought"]

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
    splited_words = [word.lower() for word in text.split() if len(word) > 2 and not word.isupper() and word not in stopwords and word.isalpha()]
    return list(dict.fromkeys(splited_words))

def save_words_into_csv(words: list[str], year: str) -> None:
    with open(f'{year}.csv', 'w') as f:
        header = ["word", "pos", "year"]
        writer = csv.writer(f)
        writer.writerow(header)
        for w in words:
            writer.writerow([w, "", year])


pdf = "2012.pdf"
extracted_text = extract_text_from_pdf(pdf)
words = parse_and_format_words_from_extracted_text(extracted_text)
save_words_into_csv(words, "2012")
