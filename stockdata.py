#
# From https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/
#    Using Pandas, Quandl, Matplotlib, Jupyter
#
import pandas as pd
import quandl
import datetime
import matplotlib.pyplot as plt     # matplotlib for pandas.Dataframe.plot()

# This line is necessary for the plot to appear in a Jupyter notebook
# %matplotlib inline
# Control the default size of figures in this Jupyter notebook
# %pylab inline
pylab.rcParams['figure.figsize'] = (15, 9)   # Change the size of plots

# setup parameters for quandl.get()
start = datetime.datetime(2018, 1, 1)
end = datetime.date.today()

# Use quandl API key to authenticate (https://docs.quandl.com)
quandl.ApiConfig.api_key = "zo1ZDyAjozzqeivpjCin"

# get stock data for ticker
apple = quandl.get("WIKI/AAPL", start_date=start, end_date=end)

# by defulat, qualndl.get() returns 'pandas.core.frame.DataFrame'
type(apple)

# list info
apple.head()

# plot adjusted closing price
apple["Adj. Close"].plot(grid = True)
