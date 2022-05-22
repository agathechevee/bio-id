from sklearn import preprocessing
import numpy as np
import csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import datetime
from mpl_toolkits.axes_grid1 import make_axes_locatable

file_morning = pd.read_csv('280122_datalog.csv')

print(file_morning['Voltage'].min())
print(file_morning['Voltage'].max())
for column in file_morning:
    columnSeriesObj = pd.DataFrame(file_morning[column])
    columnSeriesObj['CMA_16']= columnSeriesObj.rolling(20, min_periods=2).mean()
    file_morning.insert(0,column+" CMA_16",columnSeriesObj['CMA_16'],True)

print(file_morning['Voltage'].min())
print(file_morning['Voltage'].max())
print (file_morning.head(10))
names= file_morning.columns
scaler= MinMaxScaler()
norm_array = scaler.fit_transform(file_morning)
scaled_df = pd.DataFrame(norm_array).dropna()

ROC_voltage_row = scaled_df['Voltage'].pct_change(periods=20) # rolling average of MFC voltage
scaled_df['Voltage']= ROC_voltage_row

plt.plot(scaled_df['Humidity'],label='Humidity')
plt.plot(scaled_df['Temperature'],label='Temperature')
plt.plot(scaled_df['Voltage'],label='BPV V')
plt.plot(scaled_df['Light'],label='Light')
# plt.plot(scaled_df[3],label='Naked T CMA')
# plt.plot(scaled_df[5],label='MFC Voltage CMA')
plt.grid(True)
plt.legend(loc='best')
plt.show()


