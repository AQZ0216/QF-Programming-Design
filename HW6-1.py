# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:24:09 2019

@author: user
"""
import os
import pandas as pd

DJ_day_market_cap = pd.read_csv('DJ_day_market_cap.csv')

col = DJ_day_market_cap.columns

for i in range (30):
    name = col[8*i]
    stock = DJ_day_market_cap.ix[:, 8*i : 8*i+7]
    if not os.path.exists('DJ_data'):
        os.makedirs('DJ_data')
    stock.to_csv( 'DJ_data/' + name + '.csv', index = False, header = False)