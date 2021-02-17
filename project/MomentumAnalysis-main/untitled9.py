# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:09:58 2020
Email:zuhuwang@bu.edu
@author: Zuhua Wang
"""

import concurrent.futures
import os

from Stock import Stock
from scipy.stats import linregress
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import helper
#from get_all_tickers import get_tickers as gt
#import talib
# pip install talib
from matplotlib.pylab import date2num
x=[1,2,3]
returns=[1,2,3]
slope, _, rvalue, _, _ = linregress(x, returns)
print(slope, rvalue)
print(linregress(x, returns))
a=Stock("aapl")
a.populate_df("2010-01-01")
print(a.df.index.get_loc("2012-01-03"))