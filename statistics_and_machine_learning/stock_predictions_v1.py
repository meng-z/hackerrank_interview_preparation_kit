import numpy as np

'''
Since there is a delay in SMA, when WMA > SMA, price is going up; 
when WMA < SMA, price is going down.
According to this, the transaction strategy is as follows.
1. Sell all stocks we have for the one with the most significant growth in price
2. Buy stocks as many as possible for the one with the biggest drop

Reference:
- solutions
https://datumguy.wordpress.com/2017/06/27/hackerranks-stocks-predictions-exercise-review/
https://github.com/m00nlight/hackerrank/blob/master/ai/Machine-Learning/Stock-Predictions/main.py

- about moving average
https://towardsdatascience.com/trading-toolbox-01-sma-7b8e16bd9388
https://towardsdatascience.com/trading-toolbox-02-wma-ema-62c22205e2a9
'''

# 32.8/100 failed to pass since it needs 40.0 score
def diff_between_wma_and_sma(price):
    '''
    Return the difference between weighted moving average and simple moving average
    '''
    sma = np.mean(price)
    
    weight = np.arange(1, len(price)+1)
    wma = np.dot(price, weight) / weight.sum()
    return wma - sma

def printTransactions(m, k, d, name, owned, prices):
    ans = []
    info = np.array(list(map(diff_between_wma_and_sma, prices)))
    max_info = info.max()
    min_info = info.min()
    
    # consider the case that there are multiple max/min diff (for max, just sell all; for min, just buy one)
    max_diff_idx = np.where(info == max_info)[0]
    min_diff_idx = np.where(info == min_info)[0]
    
    for idx in max_diff_idx:
        if max_info > 0 and owned[idx] > 0:
            ans.append((name[idx], 'SELL', str(owned[idx])))
            
    if min_info < 0 and m > 0:
        idx = min_diff_idx[0]
        latest_price = prices[idx][-1]
        amount = int(m / latest_price)
        if amount > 0:
            ans.append((name[idx], 'BUY', str(amount)))
        
    print(len(ans))
    for a in ans:
        print(' '.join(a))
    

if __name__ == '__main__':
    tmp = input().strip().split()
    m, k, d = float(tmp[0]), int(tmp[1]), int(tmp[2])
    name, owned, prices = [], [], []
    for _ in range(k):
        tmp = input().strip().split()
        name.append(tmp[0])
        owned.append(int(tmp[1]))
        prices.append(list(map(float, tmp[2:])))
        
    printTransactions(m, k, d, name, owned, prices)
