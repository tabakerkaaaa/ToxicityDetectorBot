from pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.pipeline import Pipeline
from sklearn.exceptions import NotFittedError

def preProcess(message):
        return message.rstrip()
class ToxicDetector:
    def __init__(self):
        self.toxic_data = pd.read_csv('labeled.csv.zip', compression='zip', names=['comment', 'toxic'], sep='\t', delimiter=',')[1:].to_numpy()
        self.pipeline = Pipeline([
            ('vec', CountVectorizer(lowercase=False, preprocessor=preProcess)),
            ('tfidf', TfidfTransformer()),
            ('clf', LogisticRegressionCV(penalty='l2', cv=30, max_iter=1000, verbose=1)),
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
