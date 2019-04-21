# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:53:28 2019

@author: user
"""

def check_num(n):
    if (n >= '0' and n <= '9') or n == '.':
        return 1
    else:
        return 0
    

import requests

url = 'https://tw.stock.yahoo.com/q/q?s='

stock = input('股票代碼: ')

html_body = requests.get(url + stock)
html_body.encoding = 'big5'
htmllist = html_body.text.splitlines()

keyword = '<td align="center" bgcolor="#FFFfff" nowrap'
n = 0
for row in htmllist:
    if keyword in row:
        n += 1
        if n == 7:
            j = 0
            while check_num(row[60+j]):
                print(row[60+j] ,end = '')
                j += 1