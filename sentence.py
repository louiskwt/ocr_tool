from transformers import pipeline

def sentence_generator(word: str, num_sentences=3):
    try:
        gpt2_generator = pipeline("text-generation", model="gpt2")
        sentences = gpt2_generator("", do_sample=True, top_k=50, temperature=0.6, max_length=128, num_return_sequences=3)
        for sentence in sentences:
            print(sentence["generated_text"])
            print("=" * 50)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Make sure you have the transformers library installed: pip install transformers")

sentence_generator("answer")