import pytest

from src.stylib import common, config
from src.stylib.common import isword, wordlen


@pytest.mark.parametrize('text', ['This is a parsing test', 'ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ τὸν'])
def test_default_model(text):
    model = common.Model()
    assert model
    assert model.config
    doc = model.nlp(text)
    for token1, token2 in zip(doc, text.split()):
        assert token1.text == token2


@pytest.mark.parametrize('text', ['This is a parsing test', 'ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ τὸν'])
def test_greek_model(text):
    cnf = config.Config('el_core_news_sm')
    model = common.Model(cnf)
    assert model
    assert model.config
    doc = model.nlp(text)
    for token1, token2 in zip(doc, text.split()):
        assert token1.text == token2


@pytest.mark.parametrize('word, val', [('test', True), ('99', True), ('-100', True), ('99.00', True),
                                       ('-99.99', True), ('+12.34', True), ('12/34', False), ('ἐποίησεν', True),
                                       ('abc_123', False), ('abc1', True)])
def test_isword(word: str, val: bool):
    assert isword(word) == val


@pytest.mark.parametrize('word, val', [('test', 4), ('99', 2), ('-100', 3), ('ἐποίησεν', 8)])
def test_wordlen(word: str, val: bool):
    assert wordlen(word) == val
