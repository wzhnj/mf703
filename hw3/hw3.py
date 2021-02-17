# Import the python libraries
from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
from scipy.stats import kendalltau, pearsonr, spearmanr
import time
import datetime
import math
import scipy.stats as si
#plt.style.use('fivethirtyeight')




def a():
    assets =  ["SPY", "^VIX"]
    
    stockStartDate = '2010-01-01'
    # Get the stocks ending date aka todays date and format it in the form YYYY-MM-DD
    today = '2020-08-31'
    
    #Create a dataframe to store the adjusted close price of the stocks
    df = pd.DataFrame()
    #Store the adjusted close price of stock into the data frame
    for stock in assets:
       df[stock] = web.DataReader(stock,data_source='yahoo',start=stockStartDate , end=today)['Adj Close']
    return df

def b(df):
    
    #returns = df.pct_change()[1:]
    returns = df.pct_change()[1:]+1
    returns["^VIX"]=df['^VIX'].pct_change()[1:]
    #print(returns_daily)
    returns['SPY'] = np.log(returns['SPY'])
    print(returns)
    for i in ["SPY","^VIX"]:
        X=returns[i].to_numpy()[:-1].reshape((-1,1))
        Y=returns[i].to_numpy()[1:]
        plt.figure()
        plt.scatter(X,Y)
        #print(X)
        #print(Y)
        #X=np.array([1,2,2,1]).reshape((-1,1))
        #Y=np.array([1,1,2,2])
        model = LinearRegression()
        model.fit(X,Y)
        print(model.coef_)
        #print("Model score: ",model.score(X,Y))
        #print(X)
        
        X2=sm.add_constant(X)
        model=sm.OLS(Y,X2)
        results=model.fit()
        print("parameters:", results.params)
        print("T-values",results.tvalues)
    #I am confuse that why the p value is small but the score is small. 

def c(df):
    #I am confuse how to get monthly data with dataframe. 
    #just raw index no percentage?
    #What is the relation between the correlation and option price model?
    #returns_daily = df.pct_change()[1:]
    
    corr = stats.pearsonr(df["SPY"],df["^VIX"])
    print("Daily_Correlation: ",corr[0],"P-value: ",corr[1])
    #returns_monthly = df[::21].pct_change()[1:]
    returns_monthly = df[::21]
    #print(returns_monthly)
    corr = stats.pearsonr(returns_monthly["SPY"],returns_monthly["^VIX"])
    print("Monthly_Correlation: ",corr[0],"P-value: ",corr[1])
    
def d(df):
    #returns_daily = df.pct_change()[1:]
    returns_daily = df
    #print(returns_daily)
    df_rolling=returns_daily[['SPY','^VIX']].rolling(64).corr()[126:]
    #print(df_rolling)
    count=1
    coef = []
    for i in df_rolling['SPY']:
        if (count%2==0):
            coef.append(i)
        count+=1
    #print(coef)
    plt.figure()
    plt.plot(coef)
    plt.axhline(y=-0.105517,color='r', linestyle = '-')
    plt.show()
    #df_rolling=df_rolling.drop(df_rolling[df_rolling['SPY']<0.0001].index)

    print(df_rolling.iloc[np.arange(0,len(df_rolling),2),:])
    df_rolling=df_rolling.iloc[np.arange(0,len(df_rolling),2),:]
    #print(df_rolling)
    df_rolling=df_rolling.droplevel(level=1)
    plt.figure()
    plt.plot(df_rolling['^VIX'])
    plt.axhline(y=-0.7525,color='r', linestyle = '-')
def e(df):
    #Just minus?
    print(df)
    returns_daily = df.pct_change()[1:]+1
    returns_daily["^VIX"]=df['^VIX']
    print(returns_daily)
    returns_daily['SPY'] = np.log(returns_daily['SPY'])
    print(returns_daily)
    realized=returns_daily[['SPY']].rolling(64).std()[63:]*math.sqrt(252)   
    print(realized)
    implied = df[['^VIX']][64:]/100
    print(implied)
    
    df['Premium']=implied['^VIX']-realized['SPY']
    print("Premium")
    print(df[64:]['Premium'])
    plt.figure()
    plt.plot(df[64:]['Premium'])
    return(df[64:]['Premium'])
    
    
def euro_vanilla_call(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call
def euro_vanilla_put(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    
    return put
def f(df):
    #what does 1M straddle mean.
    #I need to compute the price of 1M call and 1M put?
    filename="F-F_Research_Data_Factors_daily.csv"
    dfRF = pd.read_csv(filename)   
    #print(dfRF)
    dfRF['Date']=pd.to_datetime(dfRF['Date'],format='%Y%m%d')
    dfRF=dfRF.set_index("Date")
    df=pd.merge(df,dfRF,left_index=True,right_index=True)
    #print(df)
    df['portfolio_price']=euro_vanilla_call(df['SPY'], df['SPY'], 1/12, df['RF'], df['^VIX']/100)+euro_vanilla_put(df['SPY'], df['SPY'], 1/12, df['RF'], df['^VIX']/100)
    #print(df['portfolio_price'])
    return df
def g(df):
    df=f(df)
    #print(df)
    df["SPY_1M_later"]=df['SPY'].shift(periods=-21)
    #print(df)
    df["Put_Payoff"]= df['SPY']-df['SPY_1M_later']
    df.Put_Payoff[df.Put_Payoff<0]=0
    df["Call_Payoff"]= df['SPY_1M_later']-df['SPY']
    df.Call_Payoff[df.Call_Payoff<0]=0
    df["Payoff"]=df.Call_Payoff+df.Put_Payoff
    df["P&L"]=df["Payoff"]-df["portfolio_price"]
    #print(df.iloc[:2663,[0,1,7,8]])
    #print(df['P&L'].mean())
    #plt.plot(df['P&L'])
    return df
def h(df):
    df=g(df)
    #print(df.columns.values)
    df=df[64:]
    df['Premium']=e(a())
    df=df.ix[:2599,['P&L','Premium']]
    print(df)
    plt.figure()
    plt.scatter(df['Premium'],df['P&L'])
h(a())
    

    
    
    