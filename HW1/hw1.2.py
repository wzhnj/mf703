# File: a1pr2.py Assignment 1, Problem 2 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 9/21/2020
#
# Description: 
#
# Exotic option pricing via simulation
#

#S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #q: rate of continuous dividend paying asset 
    #sigma: volatility of underlying asset



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
            list1.append(list1[i]*(1+sigma*s[i]))
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
    
def b_payoff(S,K,T,sigma,number_sample):
    ''' draw histogram 
        return mean and standard deviation of payoff
    '''
    payoff_list=[]
    for i in a_generate(S,T,sigma,number_sample)[0]:
        payoff_list.append(max(K-i,0))
    #print(statistics.mean(payoff_list),statistics.stdev(payoff_list))
    
    
    #draw histogram
    #plt.hist(payoff_list)
    print()
    return (statistics.mean(payoff_list),statistics.stdev(payoff_list))    

def c_price0(S,K,T,r,sigma,number_sample):
    ''' return price of a european put option after discounted
    '''
    return(b_payoff(S,K,T,sigma,number_sample)[0]*math.exp(-r*T))
    
def black_scholes_put_div(S, K, T, r, q, sigma):
    ''' return put price calculated by black scholes model
    '''
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

def d_compare(S, K, T, r, q, sigma, number_sample):
    ''' print two put price given by two different method
    '''
    print("Black scholes result:",black_scholes_put_div(S, K, T, r, q, sigma))
    print("simulation result:",c_price0(S,K,T,r,sigma,number_sample))
#a_generate()

def e_lookback_option(S,T,sigma,number_sample):
    ''' return mean of payoff of lookback put option
    '''
    price_list=[]
    data=a_generate(S,T,sigma,number_sample)[1]
    for path in data:
        price_list.append(max(0,100-min(path)))
        #print(path)
    #print(statistics.mean(price_list))
    return statistics.mean(price_list)
def f_premium(S,K,T,r,sigma,number_sample):
    return e_lookback_option(S,T,sigma,number_sample)-c_price0(S,K,T,r,sigma,number_sample)
 
def g_compare():   
    table=[]
    for i in np.arange(0,1,0.05):
        same_sigma=[]
        same_sigma.append(c_price0(100, 100, 1,0, i, 100))
        same_sigma.append(e_lookback_option(100, 1, i, 100))
        same_sigma.append(same_sigma[1]-same_sigma[0])
        table.append(same_sigma)
    print(table)
    table=list(map(list,zip(*table)))
    print(table)
    plt.plot(table[0])
    plt.plot(table[1])
    plt.plot(table[2])



print('(a)')
#a_generate(100,1,0.25,100)
print('(b)',b_payoff(100,100,1,0.25,100))
#d_compare(100,100,1,0,0,0.25,1000)
print('(c)',c_price0(100,100,1,0,0.25,100))
print('(d)')
d_compare(100,100,1,0,0,0.25,1000)
print('(e) Mean of discounted payoff',e_lookback_option(100,1,0.25,100))
g_compare()
        
        
        
        
        
        
        
        
        
        
        
        
        