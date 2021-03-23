""" Word Count based approach """

import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):

    # Finding Common words
    intersection = set(vec1.keys()) & set(vec2.keys())

    # Product of word Counts for common words
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    # Length of individual words
    sum1 = sum([ (vec1[x]**2) for x in list(vec1.keys()) ] )
    sum2 = sum([ (vec2[x]**2) for x in list(vec2.keys()) ] )
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        # Invalid type value or 0.0
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    # Demove all not \w characters and split
    words = WORD.findall(text)
    # Dictionary of counter for those words
    return Counter(words)


def wordSim(text1: str = "" ,text2: str = ""):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = get_cosine(vector1, vector2)
    return cosine


f1 = "what a fine day"
f2 = "its nice weather"

t1 = "the place looks good"
t2 = "the place is clean"


print("Cosine Sim : {}".format(wordSim(t1, t2)))
