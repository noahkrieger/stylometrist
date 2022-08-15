import math

from src.stylib.common import Text, get_vocabulary_items, get_word_count
from src.stylib.decorators import measurement


@measurement
def get_type_token(text: Text) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return v / n


@measurement
def get_k(text: Text) -> float:
    n = get_word_count(text)
    _, vocab_i, _, v = get_vocabulary_items(text)
    k = (10_000 * (sum(i ** 2 * v for i, v in vocab_i.items()) - n)) / n ** 2
    return k


@measurement
def get_r(text: Text) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return v / math.sqrt(n)


@measurement
def get_c(text: Text, base=math.e) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return math.log(v, base)/math.log(n, base)


@measurement
def get_h(text: Text, base=math.e) -> float:
    n = get_word_count(text)
    _, vocab_i, _, v = get_vocabulary_items(text)
    return (100 * math.log(n, base))/(1 - vocab_i[1]/v)


@measurement
def get_s(text: Text) -> float:
    _, vocab_i, _, v = get_vocabulary_items(text)
    return vocab_i[2]/v


@measurement
def get_k(text: Text, base=math.e) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return math.log(v, base)/math.log(math.log(n, base), base)


@measurement
def get_ln(text: Text, base=math.e) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return (1 - v**2)/(v**2 * math.log(n, base))


@measurement
def get_entropy(text: Text, base=math.e) -> float:
    _, _, prob_i,  = get_vocabulary_items(text)
    return -100 * sum(p * math.log(p, base) for p in prob_i.values())


@measurement
def get_w(text: Text, a: int = 0) -> float:
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return n**(v - a)
















