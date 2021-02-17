# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:54:08 2020

@author: 17862
"""
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()
def a_generate(S,T,sigma,number_sample):
    ''' return [0]S_t [1]table of whole paths
        print mean of final price and variance of final price
    '''
    result_table=[]
    
    result_list=[]
    for i in range(number_sample):
        mu,nom_sigma = 0,math.sqrt(T/365)
        s=np.random.normal(mu,nom_sigma,365)
        #print(s)
        list1=[S,]
        for i in range(T*365):
            list1.append(list1[i]+(sigma*s[i]))
        result_list.append(list1[-1])
        result_table.append(list1)
        #################draw path
        #plt.plot(list1)
    
    #print (result_list)
    #plt.hist(result_list)
    #print(result_list)
    
    ###########print mean and variance
    #print('mean',statistics.mean(result_list),'variance', statistics.variance(result_list))
    return (result_list,result_table)

def b_his(S,T,sigma, number_sample):
    data=a_generate(S,T,sigma,number_sample)[0]
    #plt.hist(data)
    #print(data)
    sm.qqplot(np.array(data))

def c_lookback_option(S,T,sigma,number_sample):
    ''' return mean of payoff of lookback put option
    '''
    price_list=[]
    data=a_generate(S,T,sigma,number_sample)[1]
    for path in data:
        price_list.append(max(0,100-min(path)))
        #print(path)
    #print(statistics.mean(price_list))
    return statistics.mean(price_list)

def d_delta(S,T,sigma,number_sample):
    #data=a_generate(S,T,sigma, number_sample)[0]  
    delta=[]
    for i in np.arange(0,1,0.01):
        print(i)
        delta.append((c_lookback_option(S+i,T,sigma,number_sample) - c_lookback_option(S-i,T,sigma,number_sample))/(2*i))
    print(delta)
    plt.plot(np.arange(0,1,0.01),delta)

d_delta(100,1,10,5000)
#print(c_lookback_option(100,1,10,10000))
    
