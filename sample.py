"""Sample Implimentation of approacher"""

# ===== Count Similarity =====
# from comparisionEngine.cosine_similarity.word_count_sim import WordCountSim
# compEngine = WordCountSim()
# comp_val = compEngine.wordSim("people of earth are good","people of earth are cold")
# print("simple comparision metric : {}".format(comp_val))


# ======== Tf-Idf Sim ===========
from comparisionEngine.cosine_similarity.tfidf_sim import TfidfSim

compEngine = TfidfSim()
res = compEngine.rank_documents(
    "the earth is good",
    ["this is mars", "this is good place", "earth is nice", "earth is not nice"],
)
print(res)