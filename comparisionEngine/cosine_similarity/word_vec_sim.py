"""
Semantic document similarity using Gensim

This class is based on the Gensim Soft Cosine Tutorial notebook:
https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/soft_cosine_tutorial.ipynb

for ref
https://github.com/hrs2203/doc-similarity/blob/master/examples.ipynb

"""

from re import sub

import gensim.downloader as api
from gensim.utils import simple_preprocess
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.models import WordEmbeddingSimilarityIndex
from gensim.similarities import SparseTermSimilarityMatrix
from gensim.similarities import SoftCosineSimilarity
from gensim.models.keyedvectors import Word2VecKeyedVectors

# Import and download the most up-to-date stopwords from NLTK
# from nltk import download
# from nltk.corpus import stopwords
# download('stopwords')  # Download stopwords list.
# nltk_stop_words = set(stopwords.words("english"))

from comparisionEngine.cosine_similarity.stop_words import nltk_stop_words


class NotReadyError(Exception):
    pass


class DocSim:
    """
    Find documents that are similar to a query string.
    Calculated using word similarity (Soft Cosine Similarity) of word embedding vectors

    Example usage:

    # Use default model (glove-wiki-gigaword-50)
    docsim = DocSim()
    docsim.similarity_query(query_string, documents)

    # Or, specify a preferred, pre-existing Gensim model with custom stopwords and verbose mode
    docsim = DocSim(model='glove-twitter-25', stopwords=['the', 'and', 'are'], verbose=True)
    docsim.similarity_query(query_string, documents)

    # Or, supply a custom pre-initialised model in gensim.models.keyedvectors.Word2VecKeyedVectors format
    docsim = DocSim(model=myModel)
    docsim.similarity_query(query_string, documents)
    """

    default_model = "glove-wiki-gigaword-50"
    model_ready = False  # Only really relevant to threaded sub-class

    def __init__(self, model=None, stopwords=None, verbose=False):
        # Constructor

        self.verbose = verbose

        self._load_model(model)

        if stopwords is None:
            self.stopwords = nltk_stop_words
        else:
            self.stopwords = stopwords

    def _load_model(self, model):
        # Pass through to _setup_model (overridden in threaded)
        self._setup_model(model)

    def _setup_model(self, model):
        # Determine which model to use, download/load it, and create the similarity_index

        if isinstance(model, Word2VecKeyedVectors):
            # Use supplied model
            self.model = model
        elif isinstance(model, str):
            # Try to download named model
            if self.verbose:
                print(f"Loading word vector model: {model}")
            self.model = api.load(model)
            if self.verbose:
                print("Model loaded")
        elif model is None:
            # Download/use default GloVe model
            if self.verbose:
                print(f"Loading default GloVe word vector model: {self.default_model}")
            self.model = api.load(self.default_model)
            if self.verbose:
                print("Model loaded")
        else:
            raise ValueError("Unable to load word vector model")

        self.similarity_index = WordEmbeddingSimilarityIndex(self.model)

        self.model_ready = True

    def preprocess(self, doc: str):
        # Clean up input document string, remove stopwords, and tokenize
        doc = sub(r"<img[^<>]+(>|$)", " image_token ", doc)
        doc = sub(r"<[^<>]+(>|$)", " ", doc)
        doc = sub(r"\[img_assist[^]]*?\]", " ", doc)
        doc = sub(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            " url_token ",
            doc,
        )

        return [
            token
            for token in simple_preprocess(doc, min_len=0, max_len=float("inf"))
            if token not in self.stopwords
        ]

    def _softcossim(self, query: str, documents: list):
        # Compute Soft Cosine Measure between the query and each of the documents.
        query = self.tfidf[self.dictionary.doc2bow(query)]
        index = SoftCosineSimilarity(
            self.tfidf[[self.dictionary.doc2bow(document) for document in documents]],
            self.similarity_matrix,
        )
        similarities = index[query]

        return similarities

    def similarity_query(self, query_string: str, documents: list):
        """
        Run a new similarity ranking, for query_string against each of the documents

        Arguments:
            query_string: (string)
            documents: (list) of string documents to compare query_string against
            explain: (bbol) if True, highest scoring words are also returned

        Returns:
            list: similarity scores for each of the documents
            or
            NotReadyError: if model is not ready/available
        """

        if self.model_ready:

            corpus = [self.preprocess(document) for document in documents]
            query = self.preprocess(query_string)

            if set(query) == set([word for document in corpus for word in document]):
                raise ValueError(
                    "query_string full overlaps content of document corpus"
                )

            if self.verbose:
                print(f"{len(corpus)} documents loaded into corpus")

            self.dictionary = Dictionary(corpus + [query])
            self.tfidf = TfidfModel(dictionary=self.dictionary)
            self.similarity_matrix = SparseTermSimilarityMatrix(
                self.similarity_index, self.dictionary, self.tfidf
            )

            scores = self._softcossim(query, corpus)

            return scores.tolist()

        else:
            raise NotReadyError("Word embedding model is not ready.")