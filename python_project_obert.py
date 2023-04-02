#----------------------------------------------------------------------------------------------------------------#
#    FINAL VERSION        PYTHON PROJECT
#----------------------------------------------------------------------------------------------------------------#

#Group member: Mathéo Langlais, Luc Obert, Benjamin Morlot, Quentin Le Gangneux & Martin Bouteleux

#Objective of this python code:
#It will first calculate a short and long moving average. Then it will show the price evolution of the last 10 years for each stock but it will also plot the moving average
#Then, we did a backtesting to see what was our portfolio performance if we bought 3500 stock of each stock.
#Then we plot a graph of the performance of each stock for the last ten years but it also show all the buy and sell order.
#During the next step, we calculated the average annual return of each stock
#Finally, we calculated, for each stock, the value of one put european option (the objective of this is to cover your long) if you decide to invest today.

#These packages need to be installated
#pip install pandas_datareader
#pip install yfinance
#pip install matplotlib
#pip install pandas
#pip install numpy
#pip install scipy

#Packages
import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as si
import pandas as pd
yf.pdr_override()
from datetime import datetime
from datetime import date
from datetime import timedelta

# Define variables 
#It is possible to apply this strategy on any other stock. To do so, you need to pick a ticker on Yahoo Finance. Then, you add the ticker name in the line below and it will automatically calculate the moving average, the average annual return and the value of one put european option to cover your long.
tickers = ['WMT', 'KO', 'SBUX', 'MCD']
short_window = 20
long_window = 100
initial_capital= float(100000.0)

# Loop through tickers and retrieve data
for tick in tickers:
    # Loop through tickers and retrieve data

    # ----- Retrieve data -----

    data = pdr.get_data_yahoo(tick, start=datetime(2013, 1, 1), end=datetime(2023, 1, 3))

    # ----- Signals creation -----

    # Initialize the `signals` DataFrame with the `signal` column
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create moving averages
    signals['short_mavg'] = data['Adj Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Adj Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    # ----- Ploting the signals and moving averages -----
     
     
    # Show the plot
    plt.show()
 


    # Initialize the plot figure
    fig = plt.figure()

    # Add a subplot and label for y-axis
    ax1 = fig.add_subplot(111,  ylabel='Price in $')

    # Plot the closing price
    data['Adj Close'].plot(ax=ax1, color='k', lw=1.)

    # Plot the short and long moving averages
    signals[['short_mavg']].plot(ax=ax1, color='m', lw=1.)
    signals[['long_mavg']].plot(ax=ax1, color='b', lw=1.)

    # Plot the buy signals (magenta)
    ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=4, color='g')
    ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=4, color='r')
       
    # Customize the plot
 
    plt.title(f"{tick} price evolution")      
    # Show the plot
    plt.show()

    # ----- Backtesting the strategy -----

    # Create a DataFrame `positions`
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    Posize = pd.DataFrame(index=signals.index).fillna(0.0)
    portfolio = pd.DataFrame(index=signals.index).fillna(0.0)

    # Merge adjusted close from data to signals data frame
    Merged_data = pd.merge(data, signals, left_index=True, right_index=True)

    # Stop loss calculation
    SL = np.where(Merged_data['signal'] == 1.0, Merged_data['Adj Close'] * (1 - 0.2), 0.0)

    # Buy a 3500 shares
    positions[tick] = 3500*signals['signal']  

    # Initialize the portfolio with value owned
    portfolio = pd.DataFrame(positions).multiply(Merged_data['Adj Close'], axis=0)

    # Store the difference in shares owned
    pos_diff = positions.diff()

    # Add `holdings` to portfolio
    portfolio['holdings'] = (positions.multiply(Merged_data['Adj Close'], axis=0)).sum(axis=1)

    # Add `cash` to portfolio
    portfolio['cash'] = initial_capital - (pos_diff.multiply(Merged_data['Adj Close'], axis=0)).sum(axis=1).cumsum()  

    # Add `total` to portfolio
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']

    # Add `returns` to portfolio
    portfolio['returns'] = portfolio['total'].pct_change()
    
    # Create a figure
    fig = plt.figure()

    ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')

    # Plot the equity curve in dollars
    portfolio['total'].plot(ax=ax1, color='k', lw=1.)

    ax1.plot(portfolio.loc[signals.positions == 1.0].index, portfolio.total[signals.positions == 1.0], '^', markersize=4, color='g')
    ax1.plot(portfolio.loc[signals.positions == -1.0].index, portfolio.total[signals.positions == -1.0], 'v', markersize=4, color='r')

    # Customize the plot

    plt.title(f"{tick} portfolio performance")    
    # Show the plot
    plt.show()

    # ----- Compute the benefits generated by purchaisng 1,000 shares in each stocks -----
    # Calculate annual returns 
    Avg_return = portfolio['returns'].mean()
    ANNUAL =  ((Avg_return+1)**252 - 1)*100   
        
    # ----- Compute the last Black and Scholes (BS) option price -----
    
    #------------------------------------------------------------
    
    # Parameteres explanation
    
    # s: spot price (last price for each of the tickers)
    # k: strike price (10% below the spot price: the maximum tolerated risk)
    # r: risk-free (10-years USA)
    # b: cost of carry rate equitvalent to risk-free rate (we consider our stocks to not deliver any dividends)
    # sigma: volatility of the uderlying ticker
    # t: time to maturity (set to be 3/12 of a year, after 3-monts from taking the position, if it is still loosing money the option will be executed, otherwise no)
 
    #------------------------------------------------------------
    

    # Generalized BM: call (1 and 2)
    
    # Define last value of the last row of the dataset (regarding the concerned ticker)
    last_row = data.tail(1) 
    last_value = last_row.iloc[0][-4] 

    # BS volatility calculation
    t = yf.Ticker(tick) 
    df = t.history( start=datetime(2013, 1, 1),end=datetime(2023, 1, 3))
    # Calculate daily returns 
    df['daily_return'] = df['Close'].pct_change() 
    # Calculate annualized volatility 
    volatility = df['daily_return'].std() * (252**0.5) 
    
    
    # BS risk free rate calculation in percentage (average of the last 7 days)
    rf = pdr.get_data_yahoo('^TNX', start=date.today()- timedelta(days = 8), end=date.today()- timedelta(days = 1))
    adj_close_px = rf[['Adj Close']]
    avgrf = adj_close_px.mean()
    last_row_rf = rf.tail(1) 
    last_value_rf = last_row_rf.iloc[0][-0] / 100

    # BS variable definition
    s = last_value
    k = last_value*0.9
    r = last_value_rf
    t = 3 / 12 
    sigma = volatility
    b = r
    
    # BS put defintion, only the put price is calculated as only long position will be taken
    def mygput(s, k, r, b, sigma, t):
        d1 = (np.log(s / k) + t * (b + sigma ** 2 / 2)) / ( sigma * np.sqrt(t))
        d2 = d1 - sigma * np.sqrt(t)
        put = k * np.exp(-r * t) * si.norm.cdf(-d2) - s * np.exp( t * (b-r)) * si.norm.cdf(-d1)
        return put

    # ----- PRINT THE SUMMARY -----
    print(' ')
    print(' ')
    print(' ')
    print('*----------------------------------------------------------------------------------------------------------------*')
    print('REPORT - Analysis since 2013')
    print('*----------------------------------------------------------------------------------------------------------------*')
    print(' ')
    print('For ticker:')
    print(tick)
    print(' ')
    print('The average annual return with 3,5000 shares was and a beginning portfolio value of 100,000:')
    print(ANNUAL)
    print(' ')
    print('If you decided to invest in it today the value of one put european option, to cover your long, is:')
    print(mygput(s, k, r, b, sigma, t))
    print(' ')
    print(' ')
