import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.stats as si
import numpy as np
yf.pdr_override()
from datetime import datetime
from datetime import date
from datetime import timedelta

WMT = pdr.get_data_yahoo('WMT',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)

# Isolate the adjusted closing prices
adj_close_px = WMT[['Adj Close']]
# Calculate the moving average for aapl
moving_avg = adj_close_px.rolling(window=40).mean()
# Short moving window rolling mean
WMT['42'] = adj_close_px.rolling(window=40).mean()
# Long moving window rolling mean
WMT['252'] = adj_close_px.rolling(window=252).mean()
# Plot the adjusted closing price, the short and long windows of rolling means
WMT[['Adj Close', '42', '252']].plot()
 
# Show plot
plt.show()

print(WMT)


KO = pdr.get_data_yahoo('KO',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)
# Isolate the adjusted closing prices
adj_close_px = KO[['Adj Close']]
# Calculate the moving average for aapl
moving_avg = adj_close_px.rolling(window=40).mean()
# Short moving window rolling mean
KO['42'] = adj_close_px.rolling(window=40).mean()
# Long moving window rolling mean
KO['252'] = adj_close_px.rolling(window=252).mean()
# Plot the adjusted closing price, the short and long windows of rolling means
KO[['Adj Close', '42', '252']].plot()
 
# Show plot
plt.show()

print(KO)


SBUX = pdr.get_data_yahoo('SBUX',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)
# Isolate the adjusted closing prices
adj_close_px = SBUX[['Adj Close']]
# Calculate the moving average for aapl
moving_avg = adj_close_px.rolling(window=40).mean()
# Short moving window rolling mean
SBUX['42'] = adj_close_px.rolling(window=40).mean()
# Long moving window rolling mean
SBUX['252'] = adj_close_px.rolling(window=252).mean()
# Plot the adjusted closing price, the short and long windows of rolling means
SBUX[['Adj Close', '42', '252']].plot()
 
# Show plot
plt.show()

print(SBUX)


MCD = pdr.get_data_yahoo('MCD',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)
# Isolate the adjusted closing prices
adj_close_px = MCD[['Adj Close']]
# Calculate the moving average for aapl
moving_avg = adj_close_px.rolling(window=40).mean()
# Short moving window rolling mean
MCD['42'] = adj_close_px.rolling(window=40).mean()
# Long moving window rolling mean
MCD['252'] = adj_close_px.rolling(window=252).mean()
# Plot the adjusted closing price, the short and long windows of rolling means
MCD[['Adj Close', '42', '252']].plot()
 
# Show plot
plt.show()

print(MCD)




# Isolate the adjusted closing prices
adj_close_px = MCD[['Adj Close']]
# Calculate the moving average for aapl
moving_avg = adj_close_px.rolling(window=40).mean()
# Short moving window rolling mean
MCD['42'] = adj_close_px.rolling(window=40).mean()
# Long moving window rolling mean
MCD['252'] = adj_close_px.rolling(window=252).mean()
# Plot the adjusted closing price, the short and long windows of rolling means
MCD[['Adj Close', '42', '252']].plot()
 
# Show plot
plt.show()
 
 
#aapl['42max'] = adj_close_px.rolling(window=40).max()
#aapl['42min'] = adj_close_px.rolling(window=40).min()
#aapl[['Adj Close', '42', '252', '42max', '42min']].plot()
#plt.show()

MCD = pdr.get_data_yahoo('MCD',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)
print(MCD)



#   step 5 
# s: spot price
# k: strike price
# r: risk-free
# b : cost of carry rate
# sigma: volatility of uderlying asset
# t: time to maturity
#
#--------------------- possible values of b
# b = r         # european stock oprions with no-dividend
# b = r-q       # european stock options with dividends
# b = 0         # european futures options
# b = r - rj    # european currency options
 
# ----------------------------------------------------------------------------
 
# Generalized BM: call (1 and 2)

# BS define last value of the last row

last_row_WMT = WMT.tail(1) 
last_value_WMT = last_row_WMT.iloc[0][-4] 


# BS volatility calculation

WMT = yf.Ticker("WMT") 
df = WMT.history( start=datetime(2013, 1, 1),end=datetime(2023, 1, 3))
#        calculate daily returns 
df['daily_return'] = df['Close'].pct_change() 
#        calculate annualized volatility 
volatility = df['daily_return'].std() * (252**0.5) 


# BS risk free rate calculation in percentage (average of the last 7 days)

rf = pdr.get_data_yahoo('^TNX', start=date.today()- timedelta(days = 8), end=date.today()- timedelta(days = 1))

adj_close_px = rf[['Adj Close']]
avgrf = adj_close_px.mean()

last_row_rf = rf.tail(1) 
last_value_rf = last_row_rf.iloc[0][-0] / 100











#si achete (buy) de l action alors on veut couvrir une perte lie a un cours de bourse qui 
#baisserait donc on souhaite limiter notre risque maximum a 2.5% donc on veut acheter un option qui nous donne le
#droit de vendre a -2.5% du cours de bourse actuel

#si long dans l autre sens

#Programmer un IF ... pour determiner la valeur de k selon le sens dans lequel on prend notre option sur la 
#base du croisement des MMA (strategie de trading)











# BS variable definition
 
s = last_value_WMT
k = last_value_WMT*0.9
r = last_value_rf
t = 3 / 12 #arbitrarly choosen as we decide to cover our positon for maximum 3 months
sigma = volatility
b = r #european stock oprions with no-dividend


# BS call defintion

def mygcall(s, k, r, b, sigma, t):
 
    d1 = (np.log(s / k) + t * (b + sigma ** 2 / 2)) / ( sigma * np.sqrt(t))
   
    d2 = d1 - sigma * np.sqrt(t)
   
    call = s * np.exp( t * (b-r) ) * si.norm.cdf(d1) - k * np.exp(-r * t) * si.norm.cdf(d2)
   
        
    return call


# BS put defintion

def mygput(s, k, r, b, sigma, t):
 
    d1 = (np.log(s / k) + t * (b + sigma ** 2 / 2)) / ( sigma * np.sqrt(t))
   
    d2 = d1 - sigma * np.sqrt(t)
   
    put = k * np.exp(-r * t) * si.norm.cdf(-d2) - s * np.exp( t * (b-r)) * si.norm.cdf(-d1)
   
    return put

# print results









#SMA Strategy: creating signals - Exercise 8
#-----------------------------------------------------------------------------
# Initialize the short and long windows
short_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=aapl.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = aapl['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = aapl['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:]
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)  

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)

# Plot your signals - Exercise 9
#-----------------------------------------------------------------------------
# Import `pyplot` module as `plt`
import matplotlib.pyplot as plt

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')

# Plot the closing price
aapl['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals (magenta)
ax1.plot(signals.loc[signals.positions == 1.0].index,
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
         
# Plot the sell signals (black)
ax1.plot(signals.loc[signals.positions == -1.0].index,
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
         
# Show the plot
plt.show()

# Backtesting a trading strategy - Exercise 10
#-----------------------------------------------------------------------------
# Set the initial capital
initial_capital= float(100000.0)

# Create a DataFrame `positions`
positions = pd.DataFrame(index=signals.index).fillna(0.0)

# Buy a 100 shares
positions['AAPL'] = 100*signals['signal']  
 
# Initialize the portfolio with value owned  
portfolio = positions.multiply(aapl['Adj Close'], axis=0)

# Store the difference in shares owned
pos_diff = positions.diff()

# Add `holdings` to portfolio
portfolio['holdings'] = (positions.multiply(aapl['Adj Close'], axis=0)).sum(axis=1)

# Add `cash` to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(aapl['Adj Close'], axis=0)).sum(axis=1).cumsum()  

# Add `total` to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']

# Add `returns` to portfolio
portfolio['returns'] = portfolio['total'].pct_change()

# Print the first lines of `portfolio`
print(portfolio.head())


print('Result is - Generalized formula of B&S - call:')
print(mygcall(s, k, r, b, sigma, t))
print('Result is - Generalized formula of B&S - put:')
print(mygput(s, k, r, b, sigma, t))
