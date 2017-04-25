# FFTModel
Modeling Historic Stock Prices as a FFT (HMC Econ136 "Markets and Modeling")

Logfft takes natural log of the individual daily prices and plots the logarithmic growth rate as well as the fft of this.
Normalizedfft take the daily stock data and plots the change in stock price as well as the fft of this signal.
Logfft and Normalizedfft both used a DC offset by taking the mean of the signal and subtrating that from all individual data points, centering it at 0.

You can use the AAPL.txt high resolution data by uncommenting the code shown at the top for interpreting this data, or by using the uncommented code for reading data from AAPL.csv that I sent to the team in the invitaion e-mail.
