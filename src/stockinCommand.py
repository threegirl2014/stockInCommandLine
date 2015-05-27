# -*- coding: utf-8 -*- 
#!/usr/bin/python

'''
    author : threegirl2014
'''

import urllib
import string
from matplotlib.finance import stock_dt

mystock = [
           ['000963',500,23.854],
           ['002001',300,34.581]
           ]

url = "http://hq.sinajs.cn/list=\
s_sh000001,\
s_sz399001,\
s_sz000963,\
s_sh600104"

def name_in_mystock(name):
    i = 0
    for s in mystock:
        i += 1
        if name.find(s[0]) is not -1:
            return i
    return 0

data = urllib.urlopen(url).read().decode('gb2312')
print type(data)
line = data.split('\n')

for stock in line:
    stockInfo = stock.split(',')
    if stockInfo[0]:
        #var hq_str_s_sh000001="上证指数
        name  = stockInfo[0].split('_')[3].replace('"','').replace('=','   ')
        cur   = string.atof(stockInfo[1])
        wave  = string.atof(stockInfo[2])
        per   = string.atof(stockInfo[3])
        money = string.atof(stockInfo[5].replace('";',''))
        
        
        index = name_in_mystock (name)
        if index :
            mypri = mystock[index-1][2]
            mypro = (cur - mypri) * mystock[index-1][1]
            print '%s %10.2f %10.2f %10.2f %12dw %10.3f %10.2f' %(name, cur, wave, per, money, mypri, mypro)
        else:
            print '%s %10.2f %10.2f %10.2f %12dw' %(name, cur, wave, per, money)