from unicodedata import combining
import re

import spacy

import config as cnf

registry = {}

NUMBER_PATTERN = r'^[+-]{0,1}\d+\.{0,1}\d*$'


class Model(object):
    """ SpaCy Model """

    def __init__(self, config: cnf.Config = None):
        self.config = config if config else cnf.Config()

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
    if re.match(NUMBER_PATTERN, word):
        return True
    if all(w.isalnum() or combining(w) > 0 for w in word):
        return True
    return False


def wordlen(word: str) -> int:
    """ Length of a word excluding combining characters (diacritics)"""
    return len([w for w in word if w.isalnum() and not combining(w)])
