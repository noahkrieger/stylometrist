import pytest

from src.stylib import common, config


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
