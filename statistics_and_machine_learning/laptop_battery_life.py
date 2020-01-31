#!/bin/python3

import math
import os
import random
import re
import sys
import pandas as pd
import numpy as np
from sklearn import linear_model

def EDA():
    df = pd.read_csv('trainingdata.txt', names=['X', 'y'])
    # found that for y the median, 3rd quantile and max are all 8.00
    print(df.describe())
    # find the min x when y=8.00
    print(df[df['y'] == 8.00]['X'].min()) # 4.11

def train_model():
    df = pd.read_csv('trainingdata.txt', names=['X', 'y'])
    cleaned_df = df[df['y'] < 8.00]

    reg = linear_model.LinearRegression()
    reg.fit(cleaned_df['X'].values.reshape(-1, 1), cleaned_df['y'])
    return reg

if __name__ == '__main__':
    #EDA()
    timeCharged = float(input())
    MAX_Y = 8.00
    if timeCharged >= 4.11:
        print(MAX_Y)
    else:
        reg = train_model()
        print(reg.predict(np.array([timeCharged]).reshape(1, -1))[0])
