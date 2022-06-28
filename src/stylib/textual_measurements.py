from typing import Union

from src.stylib.common import Text, isword
from src.stylib.decorators import measurement


@measurement
def word_count(text: Text) -> int:
    """ Total count of words. """
    return len([t for t in text.nlp() if isword(t.text)])
