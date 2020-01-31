# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

F, N = map(int, input().split())
train = np.array([input().split() for _ in range(N)], float)
T = int(input())
test = np.array([input().split() for _ in range(T)], float)

train_X = train[:, :-1]
train_y = train[:, -1]
# since this polynomial always has an order less than 4, set degree=3
poly = PolynomialFeatures(degree=3)
poly_train_X = poly.fit_transform(train_X)
poly_test = poly.transform(test)

# since we are not expected to account for bias and variance trade-offs at this point, just use LinearRegression
reg = LinearRegression()
reg.fit(poly_train_X, train_y)

results = reg.predict(poly_test)
for result in results:
    print(result)
