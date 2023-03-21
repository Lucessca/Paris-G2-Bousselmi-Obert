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
print(WMT)


KO = pdr.get_data_yahoo('KO',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)
print(KO)


SBUX = pdr.get_data_yahoo('SBUX',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)
print(SBUX)


MCD = pdr.get_data_yahoo('MCD',
                          start=datetime(2013, 1, 1),  ##(yyyy, dd, mm)
                          end=datetime(2023, 1, 3))     ##(yyyy, dd, mm)
print(MCD)
