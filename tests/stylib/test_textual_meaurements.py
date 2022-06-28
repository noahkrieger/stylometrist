import pytest

from src.stylib import textual_measurements
from src.stylib.common import registry


@pytest.mark.parametrize('text', ['This is a parsing test', 'ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ'])
def test_word_count(text):
    assert textual_measurements.word_count(text) == 5
    assert registry['word_count']
