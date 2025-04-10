

def make_snippet(text):
    split_text = text.split(' ')
    if len(split_text) >= 5:
        return ' '.join(split_text) + '...'
    return text




def count_words(text):
    return len([words for words in text.split() if not words.isdigit()])
    