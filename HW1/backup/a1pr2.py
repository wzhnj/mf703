# File: a1pr2.py Assignment 1, Problem 2 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 9/21/2020
#
# Description: 
#
# Exotic option pricing via simulation
#
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()
def a_generate():
    result_table=[]
    
    result_list=[]
    for i in range(100):
        mu,sigma = 0,math.sqrt(1/365)
        s=np.random.normal(mu,sigma,365)
        #print(s)
        list1=[100,]
        for i in range(365):
            list1.append(list1[i]*(1+0.25*s[i]))
        result_list.append(list1[-1])
        result_table.append(list1)
        plt.plot(list1)
    #print (result_list)
    #plt.hist(result_list)
    #print(result_list)
    return (result_list,result_table)
    
def b_payoff():
    payoff_list=[]
    for i in a_generate()[0]:
        payoff_list.append(max(100-i,0))
    #print(statistics.mean(payoff_list),statistics.stdev(payoff_list))
    #plt.hist(payoff_list)
    return (statistics.mean(payoff_list),statistics.stdev(payoff_list))    

def c_price0():
    return(b_payoff()[0]*math.exp(0))
    
def black_scholes_put_div(S, K, T, r, q, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #q: rate of continuous dividend paying asset 
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-q * T) * si.norm.cdf(-d1, 0.0, 1.0))
    
    return put

def d_compare():
    
    print("Black scholes result:",black_scholes_put_div(100, 100, 1, 0, 0, 0.25))
    print("simulation result:",c_price0())
#a_generate()

def e_lookback_option():
    price_list=[]
    data=a_generate()[1]
    for path in data:
        price_list.append(max(0,100-min(path)))
        #print(path)
    #print(statistics.mean(price_list))
    return statistics.mean(price_list)
def f_premium():
    return e_lookback_option()-c_price0()
    



print(f_premium())