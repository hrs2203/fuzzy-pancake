"""Sample Implimentation of approacher"""

# ===== Load data ===========
# from dataset.loaddataset import read_csv_file_parsed, create_one_index_for_sts

# parsed_data = create_one_index_for_sts(
#     read_csv_file_parsed("./dataset/sts_twitter.csv")
# )

# ===== Count Similarity =====
# from comparisionEngine.cosine_similarity.word_count_sim import WordCountSim

# compEngine = WordCountSim()
# calculated_values = []
# size = min(100, len(parsed_data))
# for data in parsed_data[:]:
#     comp_val = compEngine.wordSim(data["sentence1"], data["sentence2"])
#     calculated_values.append((comp_val - data["score"]))
#     print(
#         "abs: {:.2f},calculation: {:.2f}, expected: {:.2f} dif: {:.2f},".format(
#             abs(comp_val - data["score"]), comp_val, data["score"], (comp_val - data["score"])
#         )
#     )
# print(sum(calculated_values) / size)


# ======== Tf-Idf Sim ===========
# from comparisionEngine.cosine_similarity.tfidf_sim import TfidfSim
# compEngine = TfidfSim()
# for data in parsed_data[:10]:
#     comp_metric = compEngine.rank_documents(data["sentence1"], [data["sentence2"]])[0]
#     print(
#         "abs: {:.2f},calculation: {:.2f}, expected: {:.2f} dif: {:.2f},".format(
#             abs(comp_metric - data["score"]), comp_metric, data["score"], (comp_metric - data["score"])
#         )
#     )

# ======= word vec sim ==========
# from comparisionEngine.cosine_similarity.word_vec_sim import DocSim
# compEngine = DocSim(verbose=True)
# count = 0
# for data in parsed_data[:200]:
#     try:
#         similarities = compEngine.similarity_query(data["sentence1"], [data["sentence2"]])
#         similarities = similarities[0]
#         if abs(similarities - data["score"]) <= 0.2:
#             print("{0:03}>>>".format(count), end=" ")
#             count += 1
#             print(
#                 "abs: {:.2f},calculation: {:.2f}, expected: {:.2f} dif: {:.2f}, s1: {}, s2: {}".format(
#                     abs(similarities - data["score"]),
#                     similarities,
#                     data["score"],
#                     (similarities - data["score"]),
#                     data['sentence1'],
#                     data['sentence2']
#                 )
#             )
#     except:
#         pass
