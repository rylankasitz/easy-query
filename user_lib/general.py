def trim_characters(word, chars):
    for char in chars:
        word = word.replace(char, '')
    return word