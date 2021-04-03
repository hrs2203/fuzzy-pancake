"""Sample Implimentation of approacher"""

# ===== Count Similarity =====
from comparisionEngine.cosine_similarity.word_count_sim import WordCountSim
compEngine = WordCountSim()
comp_val = compEngine.wordSim("people of earth are good","people of earth are cold")
print("simple comparision metric : {}".format(comp_val))

