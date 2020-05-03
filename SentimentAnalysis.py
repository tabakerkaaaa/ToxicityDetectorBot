import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.pipeline import Pipeline
from sklearn.exceptions import NotFittedError

def preProcess(message):
        string = str(message)
        return string.translate(str.maketrans('', '', '\n'))
class ToxicDetector:
    def __init__(self):
        self.toxic_data = pd.read_csv('labeled.csv.zip', compression='zip', names=['comment', 'toxic'], sep='\t', delimiter=',')[1:].to_numpy()
        stop_words_file = open("russian_stop_words.txt", 'r')
        raw_lines = [line.split('\n') for line in stop_words_file.readlines()]
        stopwords = frozenset(next(zip(*raw_lines)))
        print(stopwords)
        self.pipeline = Pipeline([
            ('vec', CountVectorizer(lowercase=False, preprocessor=preProcess, ngram_range=(1,2), stop_words=stopwords)),
            ('tfidf', TfidfTransformer()),
            ('clf', LogisticRegressionCV(penalty='l1', cv=15, max_iter=300, verbose=1, solver='liblinear')),
        ])
    def fitPipeline(self):
        X = self.toxic_data[:, 0]
        y = self.toxic_data[:, 1].astype('double')
        self.pipeline.fit(X, y)
    def resultedToxicity(self, message):
        try:
            return self.pipeline.predict_proba([message])[0][1]
        except NotFittedError:
            return -1
