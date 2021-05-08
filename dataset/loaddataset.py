import os


def read_csv_file_parsed(file_path):
    if os.path.isfile(file_path):
        file_content = ""
        with open(file_path, "r") as file_obj:
            file_content = file_obj.read()
        file_lines = file_content.split("\n")[:-1]
        return [line.split(",") for line in file_lines]

    return []

def read_tsv_file_parsed(file_path):
    if os.path.isfile(file_path):
        file_content = ""
        with open(file_path, "r") as file_obj:
            file_content = file_obj.read()
        file_lines = file_content.split("\n")[:-1]
        return [line.split("	") for line in file_lines]

    return []

def data_corpus_to_train(parsed_data):
    resp_corpus = []
    for item in parsed_data:
        resp_corpus.append(item[1])
        resp_corpus.append(item[2])

    return resp_corpus

def create_one_index_for_sts(parsed_data):
    return [
        {"score": float(item[0]) / 5.0, "sentence1": item[1], "sentence2": item[2]}
        for item in parsed_data
    ]


# parsed_data = create_one_index_for_sts(read_csv_file_parsed("./sts_twitter.csv"))
# print(len(parsed_data))