import math

from .common import Text, get_vocabulary_items, get_word_count
from .decorators import measurement


@measurement
def get_type_token_ratio(text: Text) -> float:
    """ Calculates the Type Token Ratio (TTR) measure of vocabulary richness.  TTR is size of vocabulary divided
    by number of words in the text.

    .. math::

        \\text{Type-Token} = V/N

    Where :math:`V` is the total number of vocabulary items in a
    text and :math:`N` is the total number of words in a text.


    :param text: The text to be analyzed
    :type text: Text

    :return: The calculated Type Token
    :rtype: float

    """
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return v / n


@measurement
def get_K(text: Text) -> float:
    """ get k
    get k

    .. math::

          K = 10^4\\frac{\\sum_{i=1}^v i^2V(i,N)-N}{N^2}


    $$K = 10^4\\frac{\\sum_{i=1}^v i^2V(i,N)-N}{N^2}$$


    """
    n = get_word_count(text)
    _, vocab_i, _, v = get_vocabulary_items(text)
    k = (10_000 * (sum(i ** 2 * v for i, v in vocab_i.items()) - n)) / n ** 2
    return k


@measurement
def get_R(text: Text) -> float:
    """ get r """
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return v / math.sqrt(n)


@measurement
def get_C(text: Text, base=math.e) -> float:
    """ get c



    """
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return math.log(v, base)/math.log(n, base)


@measurement
def get_H(text: Text, base=math.e) -> float:
    n = get_word_count(text)
    _, vocab_i, _, v = get_vocabulary_items(text)
    return (100 * math.log(n, base))/(1 - vocab_i[1]/v)


@measurement
def get_S(text: Text) -> float:
    _, vocab_i, _, v = get_vocabulary_items(text)
    return vocab_i[2]/v


@measurement
def get_k(text: Text, base=math.e) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return math.log(v, base)/math.log(math.log(n, base), base)


@measurement
def get_LN(text: Text, base=math.e) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return (1 - v**2)/(v**2 * math.log(n, base))


@measurement
def get_entropy(text: Text, base=math.e) -> float:
    _, _, prob_i,  = get_vocabulary_items(text)
    return -100 * sum(p * math.log(p, base) for p in prob_i.values())


@measurement
def get_W(text: Text, a: int = 0) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return n**(v - a)
















