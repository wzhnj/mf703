# File: hw1.1.py Assignment 1, Problem 1 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 9/20/2020
#
# Description: 
#
# Historical Analysis of Sector ETFs
#
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import datetime
from scipy.stats.stats import pearsonr
from sklearn.linear_model import LinearRegression

def a_CheckData(filename):
    ''' return the file data as dataframe.
        input filename
    '''
    df = pd.read_csv(filename)   
    #df.insert(0,'city',range(2697))
    #print (df.head())
    #df=pd.DataFrame({"name":["zuhua","anlan"],"age":[22,21]},columns=['name','age'])
    df['return_percentage']=(df["Close"]-df["Open"])/df['Open']
    #print(df[df.isnull().values==True])
    #print(df["return"].head(10))
    return df
    
#a_CheckData("SPY.csv")

def b_annualized_return(filename):
    ''' return annualized return.
        input filename
    '''
    df = a_CheckData(filename)
    average_of_return_percentage = df['return_percentage'].mean()
    #print(average_of_return_percentage)
    return average_of_return_percentage*250

def b_annualized_standard_deviation(filename):
    ''' return annualized standard deviation 
        input filename
    '''
    df = a_CheckData(filename)
    std_of_return_percentage = df['return_percentage'].std()
    return std_of_return_percentage*math.sqrt(2)

def c_covariance_matrix(*filenames):
    ''' return covariance matrix for daily[0] and monthly[1]
        input one or more filenames.
    '''
    daily_return_percent=pd.DataFrame()
    monthly_return_percent=pd.DataFrame()
    for filename in filenames:
        df = a_CheckData(filename)
        daily_return_percent[filename]=df['return_percentage']
        #df['month_year']= pd.to_datetime(df['Date']).dt.to_period('M')
        df['Date']=pd.to_datetime(df['Date'])
        df=df.set_index('Date')
        #print(df)
        #print(df['2014'])
        #print(df.resample('M').sum())
        monthly_return_percent[filename]=df.resample('M').sum()['return_percentage']
        #print(df)
        #print(df['month_year']=2010-01)
   # print(monthly_return_percent.cov())
    return (daily_return_percent.cov(),monthly_return_percent.cov())

def d_correlation(*filenames):
    ''' return correlation coefficient between input and SPY.csv
        input one or more filenames
    '''
    df=a_CheckData('SPY.csv')
    df['Date']=pd.to_datetime(df['Date'])
    result_table=[]
    for filename in filenames:
        df1=a_CheckData(filename)
        df1['Date']=pd.to_datetime(df1['Date'])
        #print(df['Date'][1]-df['Date'][0]>=datetime.timedelta(days=1))
        i=0
        result_list=[]
        while(df['Date'][len(df)-1]-df['Date'][i]>=datetime.timedelta(days=90)):
            initial=i
            count=i
            SPY=[]
            new=[]
            while (df['Date'][count]-df['Date'][initial]<=datetime.timedelta(days=90)):
                SPY.append(df['return_percentage'][count])
                #print(type(df['return_percentage'][count]))
                count+=1
            initial=i
            count=i
            while (df1['Date'][count]-df1['Date'][initial]<=datetime.timedelta(days=90)):
                new.append(df1['return_percentage'][count])
                #print(type(df['return_percentage'][count]))
                count+=1
            #print(i,len(SPY))
            #print(pearsonr(SPY,new)[0])
            result_list.append(pearsonr(SPY, new)[0])
            #print(np.corrcoef(SPY,new))
            i=i+1
        result_table.append(result_list)
    #print(len(df))
    return result_table

def e_beta(*filenames):
    ''' the first one of each sublist is the entire historical period's Beta
        the following are 90 days
        input one or more filenames
        output nest list
    '''
    
    df=a_CheckData('SPY.csv')
    df['Date']=pd.to_datetime(df['Date'])
    result_table=[]
    for filename in filenames:
        df1=a_CheckData(filename)
        df1['Date']=pd.to_datetime(df1['Date'])
        y=df1['return_percentage'].to_numpy()
        x=df['return_percentage'].to_numpy().reshape((-1,1))
        model = LinearRegression()
        model.fit(x,y)
        #print(model.coef_)
        
        i=0
        #print(type(model.coef_[0].item()))
        result_list=[model.coef_,]
        while(df['Date'][len(df)-1]-df['Date'][i]>=datetime.timedelta(days=90)):
            initial=i
            count=i
            SPY=[]
            new=[]
            while (df['Date'][count]-df['Date'][initial]<=datetime.timedelta(days=90)):
                SPY.append(df['return_percentage'][count])
                #print(type(df['return_percentage'][count]))
                count+=1
            initial=i
            count=i
            while (df1['Date'][count]-df1['Date'][initial]<=datetime.timedelta(days=90)):
                new.append(df1['return_percentage'][count])
                #print(type(df['return_percentage'][count]))
                count+=1
            #print(i,len(SPY))
            #print(pearsonr(SPY,new)[0])
            y=np.asarray(new)
            x=np.asarray(SPY).reshape((-1,1))
            model = LinearRegression()
            model.fit(x,y)
            result_list.append(model.coef_[0].item())
            #print(np.corrcoef(SPY,new))
            i=i+1
        result_table.append(result_list)
    #print(len(df))
    return result_table
        
def f_auto_correlation(*filenames):
    ''' return auto correlation coefficient 
        input one or more filename
    '''
    result_list=[]
    for filename in filenames:
        df=a_CheckData(filename)
        x=df['return_percentage'].to_numpy()[:-1].reshape((-1,1))
        y=df['return_percentage'].to_numpy()[1:]
        model = LinearRegression()
        model.fit(x,y)
        result_list.append(model.coef_.item())
    return result_list
        
        
        
        
        

print('(b).','Annulized standard deviation of SYP:',b_annualized_standard_deviation("SPY.csv"))
print()
print('(c). 10 ETFs covariance matrix')
print(c_covariance_matrix('SPY.csv','XLB.csv','XLE.csv','XLF.csv','XLI.csv','XLK.csv','XLP.csv','XLU.csv','XLV.csv','XLY.csv'))
#print(c_covariance_matrix('SPY.csv','XLB.csv','XLE.csv','XLF.csv','XLI.csv','XLK.csv','XLP.csv','XLU.csv','XLV.csv','XLY.csv'))   

print()


# test D
'''
print('(d). correlation between PSY and the other 9 ETFs\n See plot\n Time consuming, please wait')
#list1=d_correlation('XLB.csv','XLE.csv')
#print(list1)
list1=d_correlation('XLB.csv','XLE.csv','XLF.csv','XLI.csv','XLK.csv','XLP.csv','XLU.csv','XLV.csv','XLY.csv')
plt.plot(list1[0])
plt.plot(list1[1])
plt.plot(list1[2])
plt.plot(list1[3])
plt.plot(list1[4])
plt.plot(list1[5])
plt.plot(list1[6])
plt.plot(list1[7])
plt.plot(list1[8])

print()

'''


# test E

print('(e). Time consuming. Please wait. See the plot')
a=e_beta('XLB.csv','XLE.csv','XLF.csv','XLI.csv','XLK.csv','XLP.csv','XLU.csv','XLV.csv','XLY.csv')
for i in a:
    plt.plot(i)
#print(type(a),type(a[0]))
'''
#print('(e).', a)



#test f
print('(f). ',f_auto_correlation('SPY.csv','XLB.csv','XLE.csv','XLF.csv','XLI.csv','XLK.csv','XLP.csv','XLU.csv','XLV.csv','XLY.csv'))
'''