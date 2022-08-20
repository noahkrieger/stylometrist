from collections import Counter
from typing import List, Tuple

import numpy as np

from .common import Text, sentence_length_in_words, distribution, \
    sentence_length_in_characters, range_distribution
from .decorators import measurement


@measurement
def average_sentence_length_in_words(text: Text) -> float:
    """ Returns the average sentence length of the text.  Defined as the total number of words divided by
     the total number of sentences. """
    sent_cnt = word_cnt = 0
    for sent in text.nlp().sents:
        sent_cnt += 1
        word_cnt += sentence_length_in_words(sent)
    return word_cnt / sent_cnt


@measurement
def sentence_length_in_words_distribution(text: Text, min_length: int = 1,
                                          max_length: int = 100) -> List[Tuple[int, float]]:
    """ Returns the distribution of sentence word lengths.  Only includes
    sentence lengths in words that are greater than or equal to the min length and less than the
    max length. """
    dist = Counter()
    for sent in text.nlp().sents:
        slen = sentence_length_in_words(sent)
        if min_length <= slen < max_length:
            dist[slen] += 1
    return distribution(dist)


@measurement
def average_sentence_length_in_characters(text: Text, exclude_combining: bool = True) -> float:
    """ Returns the average number of characters per sentence.  Defined as the total number of
    characters in a text divided by the total number of sentences."""
    chars = []
    for sent in text.nlp().sents:
        count = sentence_length_in_characters(sent.text, exclude_combining)
        chars.append(count)
    return np.mean(chars)


@measurement
def sentence_length_in_characters_distribution(text: Text, min_length: int = 1, max_length: int = 100_000,
                                               interval: int = 1,
                                               exclude_combining: bool = True) -> List[Tuple[int, int, float]]:
    """ Returns a distribution of sentence lengths in characters.  Only includes sentence lengths in
    characters that are greater than or equal to the min length and less than the max length. Interval determines
    the character range of each bucket in the distribution (i.e, an interval of 10 results in buckets of
    1 to 10, 11 to 20, etc.)"""
    dist = Counter()
    for sent in text.nlp().sents:
        slen = sentence_length_in_characters(sent.text, exclude_combining)
        if min_length <= slen < max_length:
            dist[(slen//interval * interval + 1, (slen//interval + 1) * interval)] += 1
    return range_distribution(dist)

