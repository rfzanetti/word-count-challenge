import re
import string


def count_words(words):

    base_delimiters = string.punctuation + string.whitespace

    # in order to count words with hyphen (e.g. runner-up) and apostrophe (e.g. let's),
    # we don't use them as delimiters
    delimiters = base_delimiters.replace("-", "").replace("'", "")

    split_pattern = r"[" + re.escape(delimiters) + r"]+"
    split_words = re.split(split_pattern, words)

    # re.split() returns an empty string as the last element if the text ends with a delimiter
    non_empty_words = [word for word in split_words if word]

    return len(non_empty_words)
