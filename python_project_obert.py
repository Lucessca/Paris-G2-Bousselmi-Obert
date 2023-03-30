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

print('Result is - Generalized formula of B&S - call:')
print(mygcall(s, k, r, b, sigma, t))
print('Result is - Generalized formula of B&S - put:')
print(mygput(s, k, r, b, sigma, t))
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
def mygcall(s, k, r, b, sigma, t):
 
    d1 = (np.log(s / k) + t * (b + sigma ** 2 / 2)) / ( sigma * np.sqrt(t))
   
    d2 = d1 - sigma * np.sqrt(t)
   
    call = s * np.exp( t * (b-r) ) * si.norm.cdf(d1) - k * np.exp(-r * t) * si.norm.cdf(d2)
   
        
    return call

#get spot price
#get the last row of the dataframe 
last_row_WMT = WMT.tail(1) 
#retrieve the last value of the last row 
last_value_WMT = last_row_WMT.iloc[0][-4] 

print(last_value_WMT)
#retrieve the last value of the last row 



WMT = yf.Ticker("WMT") 

df = aapl.history( start=datetime(2013, 1, 1),end=datetime(2023, 1, 3))

 

# calculate daily returns 

df['daily_return'] = df['Close'].pct_change() 



# calculate annualized volatility 

volatility = df['daily_return'].std() * (252**0.5) 
print(volatility)
 


# print the result 

print("Annualized volatility:", volatility) 
# to test:
s = last_value_WMT
k = last_value_WMT*0,9
r = .025
t = 3 / 12
sigma = volatility
b= 0

print('Result is - Generalized formula of B&S - call:')
print(mygcall(s, k, r, b, sigma, t))
# 2.45
 
 
# Generalized BM: put (1 and 2)
def mygput(s, k, r, b, sigma, t):
 
    d1 = (np.log(s / k) + t * (b + sigma ** 2 / 2)) / ( sigma * np.sqrt(t))
   
    d2 = d1 - sigma * np.sqrt(t)
   
    put = k * np.exp(-r * t) * si.norm.cdf(-d2) - s * np.exp( t * (b-r)) * si.norm.cdf(-d1)
   
    return put
 
WMT.to_csv('WMT.csv', index =False)
# to test:
s = 20
k = 20
r = .15
t = 9 / 12
sigma = 0.40
b=0
 
print('Result is - Generalized formula of B&S - put:')
print(mygput(s, k, r, b, sigma, t))
 
# 2.45
 
#--------------------------  Exercise 14, question 3
s = 110
k = 100
r = .10
q = .08
t =  6/ 12
sigma = .25
b = r - q
 
 
print('Result is - Ex 14 - question3 - european  stock option with dividend "call" :')
print(mygcall(s, k, r, b, sigma, t))
# 13.56
