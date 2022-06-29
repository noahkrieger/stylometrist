from collections import Counter
from typing import Union, List, Tuple

from src.stylib.common import Text, isword, wordlen
from src.stylib.decorators import measurement


@measurement
def word_count(text: Text) -> int:
    """ Total count of words. """
    return len([t for t in text.nlp() if isword(t.text)])


@measurement
def average_word_length(text: Text) -> float:
    """ Total number of digits and graphemes in text divided by the total number of words """
    total_len = words = 0
    for token in text.nlp():
        total_len += wordlen(token.text)
        if isword(token.text):
            words += 1
    if words == 0:
        return 0
    return total_len/words


@measurement
def word_length_distribution(text: Text, min_length: int = 1, max_length: int = 100) -> List[Tuple[int, float]]:
    dist = Counter()
    for token in text.nlp():
        wlen = wordlen(token.text)
        if min_length <= wlen < max_length:
            dist[wlen] += 1
    n = sum(dist.values())
    return [(k, v/n) for k, v in dist.items()]




