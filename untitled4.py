from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import math

assets =  ["MRK"]
price=[]
for i in range(1979,1999):
    #Get the stock starting date
    stockStartDate = str(i)+'-01-01'
    # Get the stocks ending date aka todays date and format it in the form YYYY-MM-DD
    today = str(i+1)+'-01-01'
    
    #Create a dataframe to store the adjusted close price of the stocks
    df = pd.DataFrame()
    #Store the adjusted close price of stock into the data frame
    for stock in assets:
       df[stock] = web.DataReader(stock,data_source='yahoo',start=stockStartDate , end=today)['Adj Close']
    price.append(df.iloc[0]["MRK"])
#print(df)
df=pd.DataFrame()
df["MRK"]=price
returns = np.log(df.pct_change()+1)
print(returns.mean())
#print(returns)
#print(df.pct_change())
#print(df.loc['1979-01-02'])
returns=df.iloc[1:3]
#print(price)