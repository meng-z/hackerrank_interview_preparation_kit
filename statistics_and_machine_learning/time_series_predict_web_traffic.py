# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# 41.95, failed to achieve the cutoff score 50.00
def preprocess(df):
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['dayofweek'] = df['date'].dt.dayofweek
    df.drop(columns='date', inplace=True)
    return df 

if __name__ == '__main__':
    N = int(input())
    raw_data = []
    for _ in range(N):
        raw_data.append(int(input()))

    df = pd.DataFrame(data=raw_data, columns=['num_sessions'])
    # note that the format of start is mm/dd/yyyy
    df['date'] = pd.date_range(start='10/1/2012', periods=len(df), freq='D')

    train = preprocess(df)
    #print(train.head())
    X = train.drop(columns='num_sessions')
    y = train['num_sessions']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = GradientBoostingRegressor(learning_rate=0.01, n_estimators=128,min_samples_leaf=5, max_depth=3)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    d = np.sum((np.absolute(y_pred - y_test)/y_test))*100
    eval_metric = 5 * max(20 - d, 0)
    #print('MAE: ', mean_absolute_error(y_pred, y_test))
    #print('d: ', d)
    #print('eval_metric: ', eval_metric)
    # after manually tuning the params, train again based on the whole train data
    model.fit(X, y)

    test = pd.DataFrame()
    test['date'] = pd.date_range(start='11/12/2015', periods=30, freq='D')
    test = preprocess(test)
    #print(test.head())
    results = model.predict(test)
    for result in results:
        print(result)
