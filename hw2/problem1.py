# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:10:07 2020

@author: 17862
"""
from sklearn import linear_model
import statsmodels.api as sm
import pylab as py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
import math
import datetime
#from scipy.stats.stats import pearsonr
from scipy import stats
from sklearn.linear_model import LinearRegression
def a_CheckData(filename):
    ''' return the file data as dataframe.
        input filename
    '''
    df = pd.read_csv(filename)   
    #print(df)
    return df

def b_covariance(df):
    print('covariance matrix')
    print(df.cov())
    print('correlation matrix')
    print(df.corr())
#a_CheckData('F-F_Research_Data_Factors_daily.csv')
    
def c_correlation(df):
    ''' return correlation coefficient between input and SPY.csv
        input one or more filenames
    '''
    df_rolling=df[['Mkt-RF','SMB','HML']].rolling(64).corr()[189:]
    print (df_rolling)
    SMB_Mkt_RF=[]
    HML_Mkt_RF=[]
    HML_SMB=[]
    count=1
    for i in df_rolling['Mkt-RF']:
        if (count%3==2):
            SMB_Mkt_RF.append(i)
        if (count%3==0):
            HML_Mkt_RF.append(i)
        count+=1
    count=1
    for i in df_rolling['SMB']:
        if (count%3==0):
            HML_SMB.append(i)
        
        count+=1
    #return 1
    plt.plot(HML_SMB)
    plt.plot(SMB_Mkt_RF)
    plt.plot(HML_Mkt_RF)
    print(HML_SMB)
    


def d_nomality(df):
    print(df)
    sm.qqplot(df['Mkt-RF'], line='45')
    sm.qqplot(df['HML'], line='45')
    sm.qqplot(df['SMB'], line='45')
    
def a1_CheckData(filename):
    ''' return the file data as dataframe.
        input filename
    '''
    df = pd.read_csv(filename)   
    df['return_percentage']=(df["Close"]-df["Open"])/df['Open']
    return df

def e_multi(*filenames):
    #print (a1_CheckData('SPY.csv')[:2684])
    count_plot=1
    for filename in filenames:
        y=a1_CheckData(filename)['return_percentage']
        y=y[:2684]
        #print (y)
        x=a_CheckData('F-F_Research_Data_Factors_daily.csv')[22127:]
        #print(x)
        x=x[['Mkt-RF','SMB','HML']]
        #print(x)
        regr = linear_model.LinearRegression()
        regr.fit(x,y)
        print ('Intercept: \n', regr.intercept_)
        print('Coefficients: \n', regr.coef_)
        
        b1=[]
        b2=[]
        b3=[]
        e=[]
        #for i in range(len(x)):
        #i=0
        #print(y[i],x.iloc[i,[1]])
        #print(y[i]+float(x.iloc[i,[1]]))
        #print(type(float(x.iloc[i,[1]])))
        
        
        for i in range(2596):
            y=a1_CheckData(filename)['return_percentage']
            y=y[:2684]
            #print (y)
            y=y[i:i+89]
            x=a_CheckData('F-F_Research_Data_Factors_daily.csv')[22127:]
            #print(x)
            x=x[['Mkt-RF','SMB','HML']]
            #print(x)
            x=x[i:i+89]
            regr = linear_model.LinearRegression()
            regr.fit(x,y)
            #print ('Intercept: \n', regr.intercept_)
            #print('Coefficients: \n', regr.coef_)
            b1.append(regr.coef_[0])
            b2.append(regr.coef_[1])
            b3.append(regr.coef_[2])
            
            #print(i)
        #p
        plt.figure(count_plot)
        #plt.subplot(len(filenames),2,count_plot)
        plt.plot(b1)
        plt.plot(b2)
        plt.plot(b3)
        count_plot+=1
        
def f_eit(*filenames):
    #print (a1_CheckData('SPY.csv')[:2684])
    count_plot=1
    for filename in filenames:
        y=a1_CheckData(filename)['return_percentage']
        y=y[:2684]
        #print (y)
        x=a_CheckData('F-F_Research_Data_Factors_daily.csv')[22127:]
        #print(x)
        x=x[['Mkt-RF','SMB','HML']]
        #print(x)
        regr = linear_model.LinearRegression()
        regr.fit(x,y)
        #print ('Intercept: \n', regr.intercept_)
        #print('Coefficients: \n', regr.coef_)
        
        
        e=[]
        #for i in range(len(x)):
        i=0
        #print(y[i],x.iloc[i,[1]])
        #print(y[i]+float(x.iloc[i,[1]]))
        #print(type(float(x.iloc[i,[1]])))
        for i in range(len(y)):
            #print(i)
            e.append (y[i]-regr.coef_[0]*float(x.iloc[i,[0]])-regr.coef_[1]*float(x.iloc[i,[1]])-regr.coef_[2]*float(x.iloc[i,[2]]))
        #e=np.random.randn(1000)+15
        #plt.subplot(len(filenames),1,count_plot)
        sm.qqplot(np.array(e))
        print ('mean: ',statistics.mean(e),'variance: ', statistics.variance(e))

#c_correlation(a_CheckData('F-F_Research_Data_Factors_daily.csv'))
#d_nomality(a_CheckData('F-F_Research_Data_Factors_daily.csv'))    
f_eit('SPY.csv','XLB.csv','XLE.csv','XLF.csv','XLI.csv','XLK.csv','XLP.csv','XLU.csv','XLV.csv','XLY.csv')
#f_eit('SPY.csv',"XLB.csv",'XLE.csv','XLF.csv','XLI.csv','XLK.csv','XLP.csv','XLU.csv','XLV.csv','XLY.csv')
