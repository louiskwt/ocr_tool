from transformers import pipeline

def sentence_generator(word: str):
    gpt2_generator = pipeline("text-generation", model="gpt2")
    sentences = gpt2_generator(word, do_sample=True, top_k=50, temperature=0.6, max_length=128, num_return_sequences=3)
    for sentence in sentences:
        print(sentence["generated_text"])
        print("=" * 50)

sentence_generator("answer")