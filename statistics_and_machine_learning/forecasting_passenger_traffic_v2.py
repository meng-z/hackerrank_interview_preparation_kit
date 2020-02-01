# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1.76
def train_model_v0(data):
    train = np.array(data)
    lm = LinearRegression()
    lm.fit(train[:, 0].reshape(-1, 1), train[:, 1])
    return lm

def preprocess(data):
    df = pd.DataFrame(data, columns=['month'])
    df['quarter'] = df['month'] % 3
    df['half'] = df['month'] % 6
    df['year'] = df['month'] % 12
    return df

def train_model(raw_data):
    data = np.array(raw_data)
    train = preprocess(data[:, 0])
    lm = LinearRegression()
    lm.fit(train, data[:, 1])
    return lm    

if __name__ == '__main__':
    N = int(input())
    data = []
    for _ in range(N):
        tmp = input().strip().split()
        data.append([int(tmp[0].replace('MonthNum_', '')), int(tmp[1])])

    lm = train_model(data)
    test_start = data[-1][0]+1
    test = np.array([i for i in range(test_start, test_start+12)])
    # for v0
    #results = lm.predict(test.reshape(-1, 1))
    test = preprocess(test)
    results = lm.predict(test)
    for result in results:
        print(result)
