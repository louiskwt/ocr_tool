from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")

def sentence_generator(word: str):
    encoder_input_str = "Generate a sentence in English." 
    input_ids = tokenizer(encoder_input_str, return_tensors="pt").input_ids
    force_words_ids = tokenizer(word, add_special_tokens=False).input_ids
    # Convert force_words_ids to a list of lists
    print(force_words_ids)
    force_words_ids = [force_words_ids]

    outputs = model.generate(
        input_ids,
        force_words_ids=force_words_ids,
        num_beams=5,
        num_return_sequences=1,
        no_repeat_ngram_size=1,
        remove_invalid_values=True,
    )
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

sentence_generator("answer")