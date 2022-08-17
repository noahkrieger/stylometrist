import pytest

from src.stylometrist.sentence_length import average_sentence_length_in_words, sentence_length_in_words_distribution, \
    average_sentence_length_in_characters, \
    sentence_length_in_characters_distribution

test_sentence = \
    'This is a very, very, very long sentence that is being used to test sentence distributions. Here\'s another ' + \
    'sentence that is also pretty long.  This is short. This too. I. That was a really short sentence. ' + \
    'Here is one more sentence. ἐν ἀρχῇ ἐποίησεν.  בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם'


def test_average_sentence_length_in_words():
    text = 'This is the first sentence. This is another sentence. ἐν ἀρχῇ ἐποίησεν.'
    assert average_sentence_length_in_words(text) == 4.0


def test_sentence_length_in_words_distribution():
    text = 'This is the first sentence. This is another sentence. ἐν ἀρχῇ ἐποίησεν.'
    dist = sentence_length_in_words_distribution(text)
    print(dist)
    assert dist == [(5, 0.3333333333333333), (4, 0.3333333333333333), (3, 0.3333333333333333)]
    assert sum(v for _, v in dist) == 1


def test_average_sentence_length_in_characters_combining():
    text = 'This is the first sentence. This is another sentence. ἐν ἀρχῇ ἐποίησεν.'
    avg_sentence_len = average_sentence_length_in_characters(text, exclude_combining=True)
    assert avg_sentence_len == 22


def test_average_sentence_length_in_characters_non_combining():
    text = 'This is the first sentence. This is another sentence. ἐν ἀρχῇ ἐποίησεν.'
    avg_sentence_len = average_sentence_length_in_characters(text, exclude_combining=False)
    assert avg_sentence_len == 24


@pytest.mark.parametrize('min_, max_, interval, exclude_combining, result',
                         [(1, 1000, 1, True,
                           [(91, 91, 0.125), (49, 49, 0.125), (15, 15, 0.125), (9, 9, 0.125), (2, 2, 0.125),
                            (33, 33, 0.125), (26, 26, 0.125), (47, 47, 0.125)]),
                          (1, 1000, 5, True,
                           [(91, 95, 0.125), (46, 50, 0.25), (11, 15, 0.125), (6, 10, 0.125), (1, 5, 0.125),
                            (31, 35, 0.125), (26, 30, 0.125)]),
                          (1, 1000, 2, True,
                           [(91, 92, 0.125), (49, 50, 0.125), (15, 16, 0.125), (9, 10, 0.125), (1, 2, 0.125),
                            (33, 34, 0.125), (25, 26, 0.125), (47, 48, 0.125)]),
                          (10, 20, 2, True, [(15, 16, 1.0)]),
                          (1, 1000, 1, False,
                           [(91, 91, 0.125), (49, 49, 0.125), (15, 15, 0.125), (9, 9, 0.125), (2, 2, 0.125),
                            (33, 33, 0.125), (26, 26, 0.125), (71, 71, 0.125)])])
def test_sentence_length_in_characters_distribution(min_, max_, interval, exclude_combining, result):
    dist = sentence_length_in_characters_distribution(test_sentence, min_length=min_, max_length=max_,
                                                      interval=interval,
                                                      exclude_combining=exclude_combining)
    assert dist == result
