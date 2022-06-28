from unicodedata import combining

import spacy

import config as cnf

registry = {}


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
    if word.startswith('-') and ''.join(word[1:]).isalnum():
        return True
    if word.startswith('+') and ''.join(word[1:]).isalnum():
        return True
    if all(w.isalnum() or combining(w) > 0 for w in word):
        return True
    return False
