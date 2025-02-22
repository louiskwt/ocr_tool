import enchant

def remove_duplicates_by_property(dict_list: list[dict], property: str) -> list[dict]:
    """
    Remove duplicates from a list of dictionary based on property name

    >>> data = [{'author': 'John', 'country': 'us'},
    ...         {'author': 'John', 'country': 'us'},
    ...         {'author': 'Mike', 'country': 'us'},
    ...         {'author': 'Mike', 'country': 'us'}]
    >>> expected = [{'author': 'John', 'country': 'us'},
    ...             {'author': 'Mike', 'country': 'us'}]
    >>> result = remove_duplicates_by_property(data, "author")
    >>> result == expected
    True
    """
    seen = set()
    unique_dicts = []
    for d in dict_list:
        value = d[property]
        if value not in seen:
            seen.add(value)
            unique_dicts.append(d) 
    return unique_dicts

def validate_word(word: str) -> bool:
    """
    Determine if a word is valid

    >>> validate_word("all")
    False
    >>> validate_word("CAT")
    True
    >>> validate_word("border")
    True
    >>> validate_word("n't")
    False
    """
    if len(word) <= 2:
        return False
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
        "hers", "herself", "it", "its", "it's", "he's", "she's", "they're", "itself", "they", "them", "their", "theirs",
        "themselves", "what", "which", "who", "whom", "this", "that", "these", "those",
        "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
        "having", "do", "does", "did", "doing", "will", "would", "shall", "should",
        "can", "could", "may", "might", "must", "ought", "’s", "n’t", "'re", " ", "cc", "ca", "'re"]
    us_dict = enchant.Dict("en_US")
    return us_dict.check(word) and word.lower() not in stopwords