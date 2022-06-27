import spacy

DEFAULT_MODEL = 'en_core_web_sm'


class Config(object):
    """ Configuration class.  Provides reasonable defaults for English. """

    def __init__(self, model=DEFAULT_MODEL):
        self.model = model
