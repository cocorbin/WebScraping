'''
This program estimates how predictive temperatures are of homicides in the city of Chicago using a
univariate regression model. Daily temperatures and monthly averages for the period 01/2001 - 02/2016
are taken from Wunderground.com, and can be replicated by the script "weather.py" Daily homicide
reports spanning the same period come from the City of Chicago Data Portal and are open access for
public use.

Data Sources:
Temperature data: https://www.underground.com
Crime rates: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present

_author_ : Chase O. Corbin
_date_ : 02/25/2016
_memo_ : Developed for the Colloquium in Practical Computing for Economists; Winter 2016
_place_: University of Chicago
_contact_: cocorbin@uchicago.edu
'''


##### Import Packages #####
import os
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices
from ggplot import *

'''
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
'''

os.chdir("/Users/cocorbin/PycharmProjects/untitled4/")

'''
Date = pd.date_range('1/1/2001', periods = 5533, freq = 'D')
Month = pd.date_range('1/2001', periods = 182, freq = 'M')
print(open('data/homicides_monthly.csv').read())
'''

m1 = pd.read_csv('data/homicides_monthly.csv', names = ['Month', 'Total'], header = 0, index_col= None, parse_dates=['Month'])
m2 = pd.read_csv('data/homicides_daily.csv', names = ['Date', 'Count'],header = 0, index_col= None, parse_dates=['Date'])
w1 = pd.read_csv('data/weather-data-monthly.csv', names = ['Month', 'Average'], header = 0, index_col= None, parse_dates=['Month'])
w2 = pd.read_csv('data/weather-data-daily.csv', names = ['Date', 'Temp'], header = 0, index_col= None, parse_dates=['Date'])

"""
m1.reset_index()
m2.reset_index()
w1.reset_index()
w2.reset_index()

print(m1, m2, w1, w2)
"""

dfM = pd.DataFrame(pd.merge(left=m1, right=w1, left_on='Month', right_on='Month'))
dfD = pd.DataFrame(pd.merge(left=m2, right=w2, left_on='Date', right_on='Date'))

print(dfM, dfD)


dfD['t2'] = dfD['Temp'] * dfD['Temp']
dfM['a2'] = dfM['Average'] * dfM['Average']


vars1 = ['Count', 'Temp']
df1 = dfD[vars1]
y1, X1 = dmatrices('Count ~ Temp', data = df1, return_type = 'dataframe')
mod1 = sm.OLS(y1, X1)
res1 = mod1.fit()
print(res1.summary())

vars2 = ['Count', 'Temp', 't2']
df2 = dfD[vars2]
y2, X2 = dmatrices('Count ~ Temp + t2', data = df2, return_type = 'dataframe')
mod2 = sm.OLS(y2, X2)
res2 = mod2.fit()
print(res2.summary())

vars3 = ['Total', 'Average']
df3 = dfM[vars3]
y3, X3 = dmatrices('Total ~ Average', data = df3, return_type = 'dataframe')
mod3 = sm.OLS(y3, X3)
res3 = mod3.fit()
print(res3.summary())

vars4 = ['Total', 'Average', 'a2']
df4 = dfM[vars4]
y4, X4 = dmatrices('Total ~ Average + a2', data = df4, return_type = 'dataframe')
mod4 = sm.OLS(y4, X4)
res4 = mod4.fit()
print(res4.summary())

'''
temps = cbook.get_sample_data('code/weather-data-monthly.csv', asfileobj=False)
homicides = cbook.get_sample_data('data/homicides_monthly.csv', asfileobj=False)

plt.plotfile(temps, cols=(0,1), delimiter=',')
plt.plotfile(homicides, cols(0,1), delimiter=',')
plt.xlabel('Time')
plt.ylabel('Temp. vs Homicide')
plt.show()

time = dfM['Month']
murders = dfM['Total']
temp = dfM['Average']
plot_m = ggplot(aes(x='time', y='murders'), data = dfM) + stat_smooth()
ggsave(plot_m, "plot_m.svg")
'''