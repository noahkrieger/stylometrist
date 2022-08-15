import pytest

import src.stylib
from src.stylib.common import registry
from src.stylib.word_length import average_word_length, word_length_distribution


def test_average_word_length():
    text = 'a bbb θεὸσ 999.99 eee888 _99999_'
    assert average_word_length(text) == 4


def test_word_length_distribution():
    text = 'a a bbb bbb bbb θεὸσ 999.99 eee888 _99999_'
    dist = word_length_distribution(text)
    assert dist == [(1, 0.2222222222222222), (3, 0.3333333333333333), (4, 0.1111111111111111), (5, 0.2222222222222222),
                    (6, 0.1111111111111111)]
    assert sum(v for _, v in dist) == 1


@pytest.mark.parametrize('text', ['This is a parsing test', 'ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ',
                                  'בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם'])
def test_word_count(text):
    assert src.stylib.word_length.word_count(text) == 5
    assert registry['word_count']