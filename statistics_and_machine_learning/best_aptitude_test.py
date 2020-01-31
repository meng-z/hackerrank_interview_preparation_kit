# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

if __name__ == '__main__':
    tests = int(input())
    for _ in range(tests):
        N = int(input())
        raw_train = []
        GPAs = list(map(float, input().strip().split()))
        raw_train.append(GPAs)
        for i in range(5):
            api = list(map(float, input().strip().split()))
            raw_train.append(api)

        train = np.array(raw_train).T
        clf = GradientBoostingRegressor()
        clf.fit(train[:,1:], train[:,0])
        feature_importances = clf.feature_importances_
        idx = np.argsort(feature_importances)[-1]
        print(idx+1)
