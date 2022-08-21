import math

from .common import Text, get_vocabulary_items, get_word_count
from .decorators import measurement


@measurement
def type_token_ratio(text: Text) -> float:
    """ Type/token ratio (TTR)

    Calculates the Type Token Ratio (TTR) measure of vocabulary richness.  TTR is size of vocabulary divided
    by number of words in the text.

    .. math::

        \\text{Type-Token} = V/N

    Where :math:`V` is the total number of vocabulary items in a
    text and :math:`N` is the total number of words in a text.


    :param text: The text to be analyzed
    :type text: Text

    :return: The calculated Type Token Ratio
    :rtype: float

    """
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return v / n


@measurement
def yule_k(text: Text) -> float:
    """ Yule's K Measure

    :param text: The text to be analyzed
    :type text: Text
    :return: The calculated K Measure
    :rtype: float

    .. math::

          K = 10^4\\frac{\\sum_{i=1}^v i^2V(i,N)-N}{N^2}

    Where $V_i$ is the number of vocabulary items that appear exactly $i$ times, $N$ is the total number of words
    in the text, and $V$ is the size of the vocabulary (unique words in the text).

    [1]G. U. Yule, The Statistical Study of Literary Vocabulary. 1944.

    [2]A. Miranda-García and J. Calle-Martín, “Yule’s Characteristic K Revisited,” Language Resources and Evaluation, vol. 39, no. 4, pp. 287–294, 2005, doi: 10.1007/s10579-005-8622-8.

    [3]K. Tanaka-Ishii and S. Aihara, “Computational Constancy Measures of Texts—Yule’s K and Rényi’s Entropy,” Computational linguistics - Association for Computational Linguistics, vol. 41, no. 3, pp. 481–502, 2015, doi: 10.1162/COLI_a_00228.


    """
    n = get_word_count(text)
    _, vocab_i, _, v = get_vocabulary_items(text)
    k = (10_000 * (sum(i ** 2 * v for i, v in vocab_i.items()) - n)) / n ** 2
    return k


@measurement
def root_type_token_ratio(text: Text) -> float:
    """ Guiraud’s root type/token ratio (RTTR)

    :param text: The text to be analyzed
    :type text: Text
    :return: The root type/token ratio
    :rtype: float

    .. math::

          R = \\frac{V}{\\sqrt{N}}

    Where $V$ is the size of the vocabulary (unique words in the text) and $N$ is the total number of words
    in the text.

    """
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return v / math.sqrt(n)


@measurement
def log_type_token_ratio(text: Text, base=10) -> float:
    """ Herdan’s log type/token ratio (LTTR)

    :param text: The text to be analyzed
    :type text: Text
    :param base: Base of the logarithm (default is 10)
    :type: base: int
    :return: The calculated LTTR Measure
    :rtype: float

    .. math::

          C = \\frac{\\log V}{\\log N}

    Where $V$ is the size of the vocabulary (unique words in the text) and $N$ is the total number of words
    in the text.

    """
    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return math.log(v, base)/math.log(n, base)


@measurement
def honore_r(text: Text, base=10) -> float:
    """ Honore's R Measure

    :param text: The text to be analyzed
    :type text: Text
    :param base: Base of the logarithm (default is 10)
    :type: base: int
    :return: The calculated Honore's R Measure
    :rtype: float

    .. math::

          R = \\frac{100 \\log N}{\\frac{1 - V_i}{V}}

    Where $V$ is the size of the vocabulary (unique words in the text),  $V_1$ is the number of vocabulary
    items that appear exactly $1$ time, and $N$ is the total number of words
    in the text.

    [1]T. Honore, “Some Simple Measures of Richness of Vocabulary,” Association for Literary and Linguistic Computing Bulletin, vol. 7, no. 2, pp. 172–177, 1979.

    [2]F. J. Tweedie and R. Harald Baayen, “How Variable May a Constant Be? Measures of Lexical Richness in Perspective,” Computers and the humanities, vol. 32, no. 5, pp. 323–352, 1998, doi: 10.1023/A:1001749303137.

    [3]R. Zheng, J. Li, H. Chen, and Z. Huang, “A framework for authorship identification of online messages: Writing-style features and classification techniques,” Journal of the American Society for Information Science and Technology, vol. 57, no. 3, pp. 378–393, 2006, doi: 10.1002/asi.20316.



    """

    n = get_word_count(text)
    _, vocab_i, _, v = get_vocabulary_items(text)
    return (100 * math.log(n, base))/(1 - vocab_i[1]/v)


@measurement
def sichel_s(text: Text) -> float:
    """Sichel's S Measure

    :param text: The text to be analyzed
    :type text: Text
    :param base: Base of the logarithm (default is 10)
    :type: base: int
    :return: The calculated Sichel's Measure
    :rtype: float

    .. math::

          S = \\frac{V_2}{V}

    Where $V$ is the size of the vocabulary (unique words in the text) and $V_2$ is the number of vocabulary
    items that appear exactly $2$ time. """

    _, vocab_i, _, v = get_vocabulary_items(text)
    return vocab_i[2]/v


@measurement
def summer_s(text: Text, base=10) -> float:
    """ Summer's S Measure

    :param text: The text to be analyzed
    :type text: Text
    :param base: Base of the logarithm (default is 10)
    :type: base: int
    :return: The calculated Summer's Measure
    :rtype: float

    .. math::

          S = \\frac{\\log \\log V}{\\log \\log N}

    Where $V$ is the size of the vocabulary (unique words in the text) and $N$ is the total number of words
    in the text. """

    n = get_word_count(text)
    _, _, _, v = get_vocabulary_items(text)
    return math.log(math.log(v, base))/math.log(math.log(n, base), base)


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
















