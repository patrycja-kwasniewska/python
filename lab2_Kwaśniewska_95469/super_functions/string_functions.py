def count_words(text):
    words = text.split()
    return len(words)


def reverse_words(text):
    words = text.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words


def remove_whitespaces(text):
    return ''.join(text.split())