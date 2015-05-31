# -*- coding: utf-8 -*- 
#!/usr/bin/python

'''
    author : threegirl2014
'''

import urllib
import string

from terminalColor import bcolors

# from matplotlib.finance import stock_dt

mystock = [
           ['000963',500,23.854],
           ['002001',300,34.581]
           ]

url = "http://hq.sinajs.cn/list=\
sh000001,\
sz399001,\
sz399006,\
sz000818,\
sz000949,\
sh600619,\
sz000877,\
sz002200,\
sh600830,\
sh601318,\
sz150019"

def name_in_mystock(name):
    i = 0
    for s in mystock:
        i += 1
        if name.find(s[0]) is not -1:
            return i
    return 0

def highOrLow(a,b):
    if a >= b:
        return bcolors.RED
    else:
        return bcolors.GREEN
    
data = urllib.urlopen(url).read().decode('gb2312')
#print type(data)
line = data.split('\n')

print "代码      名称         昨收        今开     最高        最低       现价     涨幅"

for stock in line:
    stockInfo = stock.split(',')
    if stockInfo[0]:
        #var hq_str_s_sh000001="上证指数
        temp  = stockInfo[0].split('_')[2].replace('"','').split('=')
        code = temp[0]
        name = temp[1]
        todayBeginPrice   = string.atof(stockInfo[1])
        yersterdayEndPrice  = string.atof(stockInfo[2])
        currentPrice   = string.atof(stockInfo[3])
        todayMaxPrice = string.atof(stockInfo[4])
        todayMinPrice = string.atof(stockInfo[5])
        if '%.2f' % todayBeginPrice == '0.00':
            per = u'停牌'
        else:
            per = ( '%+.2f' % ( ( currentPrice / yersterdayEndPrice - 1 ) * 100 ) )+ '%'
        
        todayBeginPriceColor = highOrLow(todayBeginPrice, yersterdayEndPrice)
        currentPriceColor = highOrLow(currentPrice, yersterdayEndPrice)
        todayMaxPriceColor = highOrLow(todayMaxPrice, yersterdayEndPrice)
        todayMinPriceColor = highOrLow(todayMinPrice, yersterdayEndPrice)
#         index = name_in_mystock (name)
#         if index :
#             mypri = mystock[index-1][2]
#             mypro = (cur - mypri) * mystock[index-1][1]
#             print '%s %10.2f %10.2f %10.2f %12dw %10.3f %10.2f' %(name, cur, wave, per, money, mypri, mypro)
        print '%s %4s %10.2f %s%10.2f%s %s%10.2f%s %s%10.2f%s %s%10.2f   %s%s' % \
            (code, 
             name, 
             yersterdayEndPrice, 
             todayBeginPriceColor, todayBeginPrice, bcolors.ENDC, 
             todayMaxPriceColor, todayMaxPrice, bcolors.ENDC, 
             todayBeginPriceColor, todayMinPrice, bcolors.ENDC, 
             currentPriceColor, currentPrice, per, bcolors.ENDC)
            
            
            
