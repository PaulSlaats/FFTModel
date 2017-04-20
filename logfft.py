#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:29:36 2017

@author: paulslaats
"""

import scipy.fftpack
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fftpack import fft

data_df = pd.read_csv('AAPL.csv')
print(data_df.columns)
AdjClose = data_df['AdjClose']

#data_df = pd.read_csv('SPY7_25_16_8_2_16.txt', sep=",")
#print(data_df.columns)
#print data_df
#AdjClose = data_df[u'Close']

# Number of sample points
N = len(AdjClose)
Nln = N - 1
AdjCloseln = np.zeros(Nln)
for i in range(0,Nln):
    AdjCloseln[i] = math.log(AdjClose[i]/AdjClose[i+1])
    
print AdjCloseln
    
mean = np.mean(AdjCloseln)
AdjCloselnmean = np.zeros(Nln)

for i in range(0,Nln):
    AdjCloselnmean[i] = AdjCloseln[i] - mean

# sample spacing
T = 1.0 / Nln
x = np.linspace(0.0, Nln*T, Nln)
yf = fft(AdjCloseln)
xf = np.linspace(0.0, 1.0/(2.0*T), Nln//2)
youtput = 2.0/Nln * np.abs(yf[0:Nln//2])

#plot stock
plt.plot(x, AdjCloseln)
plt.grid()
plt.show()

# plot ln stock
plt.plot(xf, youtput)
plt.grid()
plt.show()
