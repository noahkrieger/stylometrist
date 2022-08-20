from collections import Counter
from functools import lru_cache
from typing import List, Tuple
from unicodedata import combining
import re

import spacy

from .config import Config

registry = {}

NUMBER_PATTERN = re.compile(r'^[+-]{0,1}\d+\.{0,1}\d*$')
SENTENCE_ENDING_PATTERN = re.compile('^[¿¡]{0,1}(.*?)[.!? \n]*$')


class Model(object):
    """ SpaCy Model """

    def __init__(self, config: Config = None):
        self.config = config if config else Config()

        self._nlp = spacy.load(self.config.model)

    def nlp(self, text: str):
        return self._nlp(text)


class Text(object):
    """ Arbitrary text class. """

    def __init__(self, text: str, encoding: str = 'utf-8', model: Model = None):
        self.text = text
        self.encoding = encoding

        self.model = model if model else Model()

        self._nlp = self.model.nlp

    def nlp(self):
        return self._nlp(self.text)


def isword(word: str) -> bool:
    """ Simple test for words.  A word consists of only graphemes and numbers, except leading positive or negative
      signs.  May need to be refined for languages other than English """
    if word.isalnum():
        return True
    if NUMBER_PATTERN.match(word):
        return True
    if all(w.isalnum() or combining(w) > 0 for w in word):
        return True
    return False


def get_word_count(text: Text) -> int:
    """ Total count of words. """
    return len([t for t in text.nlp() if isword(t.text)])


@lru_cache(maxsize=10)
def get_vocabulary_items(text: Text) -> Tuple[Counter, Counter, dict, int]:
    vocab = Counter([t.text for t in text.nlp() if isword(t.text)])
    vocab_i = Counter()
    for k, v in vocab.items():
        vocab_i[v] += 1
    vocab_len = len(vocab)
    prob_i = {k: v / vocab_len for k, v in vocab_i.items()}

    return vocab, vocab_i, prob_i, vocab_len


def word_length(string: str, exclude_combining: bool = True) -> int:
    """ Length of a word, with or without combining characters (diacritics).
    A word is a 'continuous string of graphemes and/or digits.' (Grieve, 2007) """
    if exclude_combining:
        return len([s for s in string if s.isalnum() and not combining(s)])
    else:
        return len([s for s in string if s.isalnum()])


def sentence_length_in_words(sent: spacy.tokens.doc.Doc):
    """ Length of a sentence in words. """
    return len([t.text for t in sent if isword(t.text)])


def distribution(dist: Counter) -> List[Tuple[int, float]]:
    n = sum(dist.values())
    return [(k, v / n) for k, v in dist.items()]


def range_distribution(dist: Counter) -> List[Tuple[int, int, float]]:
    n = sum(dist.values())
    return [(f, t, v / n) for (f, t), v in dist.items()]


def string_length(string: str, exclude_combining: bool = True) -> int:
    """ Length of a string, with or without combining characters (diacritics).  """
    pass


def sentence_length_in_characters(sent: str, exclude_combining: bool = True) -> int:
    """ Length of a sentence in characters.  Excludes question marks, exclamation points, newlines,
    and nonabbreviatory periods. (Grieve, 2007) An attempt has been made to handle left to right
    languages and upside down question marks and exclamation points.  Needs further testing """

    # TODO: Improve implementation for better support of non-English languages

    text = SENTENCE_ENDING_PATTERN.search(sent).group(1)
    if exclude_combining:
        text = [t for t in text if not combining(t)]
    return len(text)
