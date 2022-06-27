import pytest

from src.stylib import common, classic_measurements
from src.stylib.common import registry


@pytest.mark.parametrize('text', ['This is a parsing test', 'ἐν ἀρχῇ ἐποίησεν ὁ θεὸσ'])
def test_word_count(text):
    assert classic_measurements.word_count(text) == 5
    assert registry['word_count']
