import os
import pickle
import math
import warnings
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from datasets import load_dataset

# Suppress the NotOpenSSLWarning
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

class Indexer:
    dbfile = "./ir.idx"

    def __init__(self):
        self.stopwords = stopwords.words('english')

        if os.path.exists(self.dbfile):
            # Load the existing index
            with open(self.dbfile, 'rb') as f:
                self.index = pickle.load(f)
        else:
            # Build the index
            ds = load_dataset("cnn_dailymail", '3.0.0', split="test")
            self.raw_ds = ds['article']
            self.clean_text(self.raw_ds)
            self.create_postings_lists()

    def clean_text(self, lst_text, query=False):
        # This method is to preprocess the text.
        # Tokenization, lemmatization, and stopwords removal can be done here.
        tokenizer = RegexpTokenizer(r'\w+')
        lemmatizer = WordNetLemmatizer()

        for text in lst_text:
            tokens = tokenizer.tokenize(text)
            tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in self.stopwords]
        # TODO: Further preprocessing
        return tokens

    def create_postings_lists(self):
        # TODO: This method is to create postings lists.
        pass

class SearchAgent:
    k1 = 1.5
    b = 0.75

    def __init__(self, indexer):
        self.indexer = indexer

    def query(self, q_str):
        # TODO: This method takes a user's query and retrieves relevant documents.
        pass

    def display_results(self, results):
        for docid, score in results[:5]:
            print(f'\nDocID: {docid}')
            print(f'Score: {score}')
            print('Article:')
            print(self.indexer.raw_ds[docid])

if __name__ == "__main__":
    indexer = Indexer()
    search_agent = SearchAgent(indexer)
    while True:
        query_str = input("Enter your query: ")
        search_agent.query(query_str)