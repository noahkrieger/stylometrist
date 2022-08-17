from collections import Counter
from typing import List, Tuple

from src.stylometrist.common import Text, isword, word_length, distribution, get_word_count
from src.stylometrist.decorators import measurement


@measurement
def word_count(text: Text) -> int:
    """ Total count of words. """
    return get_word_count(text)


@measurement
def average_word_length(text: Text) -> float:
    """ Total number of digits and graphemes in text divided by the total number of words """
    total_len = words = 0
    for token in text.nlp():
        total_len += word_length(token.text)
        if isword(token.text):
            words += 1
    if words == 0:
        return 0
    return total_len / words


@measurement
def word_length_distribution(text: Text, min_length: int = 1, max_length: int = 100) -> List[Tuple[int, float]]:
    """ Returns a distribution of word lengths from min_length up to but not including max_length. """
    dist = Counter()
    for token in text.nlp():
        wlen = word_length(token.text)
        if min_length <= wlen < max_length:
            dist[wlen] += 1
    return distribution(dist)