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
