#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:16:05 2017

@author: paulslaats
"""

import scipy.fftpack
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fftpack import fft

#data_df = pd.read_csv('SPY7_25_16_8_2_16.txt', sep=",")
#print(data_df.columns)
#print data_df
#AdjClose = data_df[u'Close']

data_df = pd.read_csv('AAPL.csv')
print(data_df.columns)
AdjClose = data_df['AdjClose']

# Number of sample points
N = len(AdjClose)
AdjCloseDC = np.zeros(N)
mean = np.mean(AdjClose)
for i in range(0,N):
    AdjCloseDC[i] = AdjClose[i] - mean

# sample spacing
T = 1.0 / N
x = np.linspace(0.0, N*T, N)
yf = fft(AdjCloseDC)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
youtput = 2.0/N * np.abs(yf[0:N//2])

#plot stock
plt.plot(x, AdjCloseDC)
plt.grid()
plt.show()

# plot ln stock
plt.plot(xf, youtput)
plt.grid()
plt.show()
