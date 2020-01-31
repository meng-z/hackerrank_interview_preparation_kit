# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model

# got score 63.13
def train_model():
    corpus = []
    labels = []
    with open('trainingdata.txt', 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            labels.append(int(line[0]))
            corpus.append(line[1:])

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english', max_features=10000)
    X = vectorizer.fit_transform(corpus)

    clf = linear_model.LogisticRegression(multi_class='ovr')
    clf.fit(X, labels)
    return clf, vectorizer

if __name__ == '__main__':
    clf, vectorizer = train_model()

    n = int(input())
    test = []
    for _ in range(n):
        test.append(input())

    pred = clf.predict(vectorizer.transform(test))
    for p in pred:
        print(p)
