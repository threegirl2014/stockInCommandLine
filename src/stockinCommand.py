# -*- coding: utf-8 -*- 
#!/usr/bin/python

'''
    author : threegirl2014
'''

import urllib
import string
import time
import os
import platform
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

def getTime():
    return time.strftime('%Y-%m-%d %A %p %X', time.localtime(time.time()))


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

def printStock():
    print bcolors.WHITE, "代码      名称         昨收        今开     最高        最低       现价     涨幅", bcolors.ENDC

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
            #红涨绿跌
            todayBeginPriceColor = highOrLow(todayBeginPrice, yersterdayEndPrice)
            currentPriceColor = highOrLow(currentPrice, yersterdayEndPrice)
            todayMaxPriceColor = highOrLow(todayMaxPrice, yersterdayEndPrice)
            todayMinPriceColor = highOrLow(todayMinPrice, yersterdayEndPrice)

            print '%s%s%s %s%4s%s %s%10.2f%s %s%10.2f%s %s%10.2f%s %s%10.2f%s %s%10.2f   %s%s' % \
                (bcolors.WHITE, code, bcolors.ENDC,  
                 bcolors.WHITE, name, bcolors.ENDC,  
                 bcolors.WHITE, yersterdayEndPrice, bcolors.ENDC,  
                 todayBeginPriceColor, todayBeginPrice, bcolors.ENDC, 
                 todayMaxPriceColor, todayMaxPrice, bcolors.ENDC, 
                 todayBeginPriceColor, todayMinPrice, bcolors.ENDC, 
                 currentPriceColor, currentPrice, per, bcolors.ENDC)
            
            
if __name__ == '__main__':
    while True:
        sysstr = platform.system()
        if sysstr == 'Darwin':
            i = os.system('clear')
        elif sysstr == 'Windows':
            i = os.system('cls')
        elif sysstr == 'Linux':
            i = os.system('clear')
        print bcolors.YELLOW, getTime(), bcolors.ENDC
        printStock()
        time.sleep(5)            
