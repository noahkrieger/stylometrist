from typing import Union

from src.stylib.common import Text
from src.stylib.decorators import measurement


@measurement
def word_count(text: Text):
    return len(text.nlp())
