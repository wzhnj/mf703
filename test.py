# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:46:40 2020

@author: 17862
"""
from pandas_datareader import data


def a_getdata(tickers):
    #tickers = ['SPY', 'XLB']
    source = 'yahoo'
    start_date = '01-01-2018'
    end_date = '01-01-2020'
    prices = data.DataReader(tickers, source, start_date, end_date)
    return prices

print (a_getdata(['SPY','XLB']))


