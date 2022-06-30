import pytest

from src.stylib import textual_measurements
from src.stylib.common import registry
from src.stylib.textual_measurements import average_word_length, word_length_distribution, \
    average_sentence_length_in_words, sentence_length_in_words_distribution


@pytest.mark.parametrize('text', ['This is a parsing test', 'ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ'])
def test_word_count(text):
    assert textual_measurements.word_count(text) == 5
    assert registry['word_count']


def test_average_word_length():
    text = 'a bbb θεὸσ 999.99 eee888 _99999_'
    assert average_word_length(text) == 4


def test_word_length_distribution():
    text = 'a a bbb bbb bbb θεὸσ 999.99 eee888 _99999_'
    dist = word_length_distribution(text)
    assert dist == [(1, 0.2222222222222222), (3, 0.3333333333333333), (4, 0.1111111111111111), (5, 0.2222222222222222),
                    (6, 0.1111111111111111)]
    assert sum(v for _, v in dist) == 1


def test_average_sentence_length_in_words():
    text = 'This is the first sentence. This is another sentence. ἐν ἀρχῇ ἐποίησεν.'
    assert average_sentence_length_in_words(text) == 4.0


def test_sentence_length_in_words_distribution():
    text = 'This is the first sentence. This is another sentence. ἐν ἀρχῇ ἐποίησεν.'
    dist = sentence_length_in_words_distribution(text)
    print(dist)
    assert dist == [(5, 0.3333333333333333), (4, 0.3333333333333333), (3, 0.3333333333333333)]
    assert sum(v for _, v in dist) == 1
