from transformers import pipeline

def sentence_generator(word: str, num_sentences=3):
    try:
        gpt2_generator = pipeline("text-generation", model="gpt2")
        for _ in range(num_sentences):
            result = gpt2_generator(word, do_sample=True, top_k=50, temperature=0.7, max_length=30, num_return_sequences=1, pad_token_id=50256, truncation=True)
            print(result[0]['generated_text'].strip())
            print("=" * 50)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Make sure you have the transformers library installed: pip install transformers")

sentence_generator("lucky")