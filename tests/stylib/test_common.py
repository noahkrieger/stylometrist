import pytest

from src.stylib import common, config
from src.stylib.common import isword, word_length, sentence_length_in_characters, get_vocabulary_items, Text


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
def test_word_length(word: str, val: bool):
    assert word_length(word) == val


@pytest.mark.parametrize('sent, val, excl', [('This is a test', 14, True), ('This is a test.', 14, True),
                                             ('This is a test!!!', 14, True), ('This is a test?', 14, True),
                                             ('This is a test.\n', 14, True), ('This is a test...!?', 14, True),
                                             ('T.h.i.s. is a test.', 18, True), ('This is a test...!?', 14, False),
                                             ('ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ τὸν', 27, True),
                                             ('ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ τὸν', 36, False),
                                             ('בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם, וְאֵת הָאָרֶץ', 37, True),
                                             (
                                                     'בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם, וְאֵת הָאָרֶץ.',
                                                     37, True),
                                             ('בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם, וְאֵת הָאָרֶץ.', 60,
                                              False),
                                             ('¿Es el comienzo?', 14, True),
                                             ('¡Al principio!', 12, True),
                                             ])
def test_sentence_length_in_characters(sent: str, val: int, excl: bool):
    assert sentence_length_in_characters(sent, exclude_combining=excl) == val


def test_get_vocabulary_items():
    text = Text('The The hello The hello 123 321 $.$.')
    vocab, vocab_i, prob_i, cnt = get_vocabulary_items(text)
    assert cnt == 4
    assert vocab['The'] == 3
    assert vocab['hello'] == 2
    assert vocab['123'] == 1
    assert vocab['321'] == 1
    assert vocab.get('$.$.', 0) == 0
    assert vocab_i[3] == 1
    assert vocab_i[2] == 1
    assert vocab_i[1] == 2
    assert prob_i[3] == prob_i[2] == 0.25
    assert prob_i[1] == 0.50
    assert sum(v for v in prob_i.values()) == 1
