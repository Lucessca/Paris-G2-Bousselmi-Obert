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
                          end=datetime(2023, 21, 3))     ##(yyyy, dd, mm)
print(WMT)
