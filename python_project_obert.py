#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:32:52 2023

@author: lucobert
"""

# Sock price import

import pandas_datareader.data as pdr
import yfinance as yf
yf.pdr_override()
from datetime import datetime

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

print(KO)


SBUX = pdr.get_data_yahoo('SBUX',
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
