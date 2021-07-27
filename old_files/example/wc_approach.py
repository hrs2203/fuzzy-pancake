""" Word Count based approach """
from ..cosine_similarity.word_count_sim import WordCountSim

f1 = "what a fine day"
f2 = "its nice weather"

t1 = "the place looks good"
t2 = "the place is clean"

comparator = WordCountSim()

print("Cosine Sim : {}".format(comparator.wordSim(f1, f2)))

print("Cosine Sim : {}".format(comparator.wordSim(t1, t2)))
