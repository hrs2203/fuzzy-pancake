import numpy as np
from comparisionEngine.cosine_similarity.stop_words import nltk_stop_words as stop_words

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize 

# On first executino uncomment this
# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')

class LemmaTokenizer:
    """ Interface to the WordNet lemmatizer from nltk """

    ignore_tokens = [",", ".", ";", ":", '"', "``", "''", "`"]

    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def __call__(self, doc):
        return [
            self.wnl.lemmatize(t)
            for t in word_tokenize(doc)
            if t not in self.ignore_tokens
        ]

class TfidfSim:
    tokenizer = LemmaTokenizer()
    vectorizer = TfidfVectorizer(stop_words=stop_words, tokenizer=tokenizer)


    def rank_documents(self, search_terms: str, documents: list):
        """ Search for search_terms in documents, and return a list of cosine similarity scores """

        try:
            vectors = self.vectorizer.fit_transform([search_terms] + documents)

            cosine_similarities = linear_kernel(vectors[0:1], vectors).flatten()

            document_scores = [
                item.item() for item in cosine_similarities[1:]
            ]  # convert back to native Python dtypes

        except ValueError:
            print(f"Unable to rank documents for search terms: {search_terms}")

            document_scores = [0.0 for _ in range(len(documents))]

        return document_scores