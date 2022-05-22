from sklearn import preprocessing
import numpy as np
import csv
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import datetime
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable

file_morning = pd.read_csv('280122_datalog.csv')

def y_max():
    y_axis_tick= []
    for column in file_morning:
        
        ymax= file_morning[column].max()
        y_axis_tick.append(ymax)
    return y_axis_tick
def y_min():
    y_axis_min= []
    for column in file_morning:
        ymin= file_morning[column].min()
        y_axis_min.append(ymin)
    return y_axis_min

min_list = y_min()
max_list = y_max()

for column in file_morning:
    columnSeriesObj = pd.DataFrame(file_morning[column])
    columnSeriesObj['CMA_16']= columnSeriesObj.rolling(120, min_periods=10).mean()
    file_morning.insert(0,column+" CMA_16",columnSeriesObj['CMA_16'],True)
scaler= MinMaxScaler()
norm_array = scaler.fit_transform(file_morning)
scaled_df = pd.DataFrame(norm_array).dropna()
# print(scaled_df.head(15))


fig, ax1 = plt.subplots(1,1,figsize=[7,5])
ax1.plot(scaled_df[2],'C0')
ax1.set_ylabel('BPV V CMA', color='C0')
ax1.tick_params(axis='y',color='C0', labelcolor='C0')
ax1.spines['top'].set_visible(False)
ax1.set_xticks([0,120,240,360,480,600,720,840])
# ax1.set_xticklabels(['0h', '1h', '2h', '3h', '4h','5h','6h','7h'])


ax2 = ax1.twinx()
ax2.plot(scaled_df[3],'C1')
ax2.set_ylabel('Light', color='C1')
ax2.tick_params(axis='y', color='C1', labelcolor='C1')
ax2.spines['right'].set_color('C1')
ax2.spines['left'].set_color('C0')
ax2.spines.top.set_visible(False)

ax3=ax1.twinx()
ax3.plot(scaled_df[1],'C3')
ax3.set_ylabel('Temperature', color='C3')
ax3.get_yaxis().set_visible(False)
ax3.spines.right.set_visible(False)
ax3.spines.left.set_visible(False)
ax3.spines.top.set_visible(False)

ax4=ax1.twinx()
ax4.plot(scaled_df[0],'C4')
ax4.set_ylabel('Humidity', color='C3')
ax4.get_yaxis().set_visible(False)
ax4.spines.right.set_visible(False)
ax4.spines.left.set_visible(False)
ax4.spines.top.set_visible(False)

divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.6)
cax2 = divider.append_axes("right", size="5%", pad=0.6)
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax2.get_xaxis().set_visible(False)
cax2.get_yaxis().set_visible(False)

divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="5%", pad=0.6)
cax2 = divider.append_axes("right", size="5%", pad=0.6)
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax2.get_xaxis().set_visible(False)
cax2.get_yaxis().set_visible(False)

divider = make_axes_locatable(ax3)
cax = divider.append_axes("right", size="5%", pad=0.6)
cax2 = divider.append_axes("right", size="5%", pad=0.6)
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax2.get_xaxis().set_visible(False)
cax2.get_yaxis().set_visible(False)

divider = make_axes_locatable(ax4)
cax = divider.append_axes("right", size="5%", pad=0.6)
cax2 = divider.append_axes("right", size="5%", pad=0.6)
cax.get_xaxis().set_visible(False)
cax2.get_xaxis().set_visible(False)

cax.yaxis.tick_right()
cax.yaxis.set_label_position('right')
cax.plot(scaled_df[2])
cax.set_ylim(min_list[3],max_list[3])
cax.set_yticks([min_list[3],max_list[3]])
cax.set_ylabel('Temperature (°C)', color='C3')
cax.set_yticks([0,0.25,0.5,0.75,1])
cax.set_yticklabels(['x', 'y', 'z', 'yo', 'oui'])
cax.tick_params(axis='y', color='C3', labelcolor='C3')
cax.set_xlim(2000,2001)
cax.spines.right.set_color('C3')
cax.spines.left.set_visible(False)
cax.spines.top.set_visible(False)
cax.spines.bottom.set_visible(False)

print(min,max)

cax2.yaxis.tick_right()
cax2.yaxis.set_label_position('right')
cax2.plot(scaled_df[3])
cax2.set_ylabel('Humidity (%)', color='C4')
cax2.tick_params(axis='y', color='C4', labelcolor='C4')
cax.set_ylim(min_list[2],max_list[2])
cax2.set_xlim(2000,2001)
cax2.spines.right.set_color('C4')
cax2.spines.left.set_color('white')
cax2.spines.left.set_visible(False)
cax2.spines.top.set_visible(False)
cax2.spines.bottom.set_visible(False)

plt.show()