import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import random

files = ['280122_datalog.csv','210721_MFC_recording1.3.csv','050821_night_recording.csv']
# '220721_MFC_recording_morning.csv','230721_MFC_recording_night.csv','040821_MFC_recorning_night.csv']
# #,'050821_night_recording.csv','060821_night_recording.csv']
#files = ['070821_high_humidity2.csv']

ROC = pd.DataFrame()

for i in files:
    df = pd.read_csv(i)
    print(df[:10])

    ROC_voltage_row = df['Voltage'].pct_change(periods=20) # rolling average of MFC voltage
    df = df.rolling(20).mean() #for all the other variable to also be averaged over 20 periods
    df['Voltage']= ROC_voltage_row
    df=df.dropna()
    ROC = pd.concat([ROC,df]) #collecting all ROC MFC voltage values
print(ROC[:10])
plt.plot(ROC['Humidity'],label='Humidity')
plt.plot(ROC['Temperature'],label='Temperature')
plt.plot(ROC['Voltage'],label='BPV V')
plt.plot(ROC['Light'],label='Light')
plt.grid(True)
plt.legend(loc='best')
plt.show()

bottom_100_ROC = ROC.dropna().nsmallest(100,['ROC_voltage_row']) # getting bottom worse values
top_100_ROC = ROC.dropna().nlargest(100,['ROC_voltage_row']) #getting top values
bottom_100 = bottom_100_ROC['Humidity']
top_100 = top_100_ROC['Humidity']

# scatter plot
#make x-axis value for bottom value and top value
x1 = np.full_like(bottom_100, 5)
jitter = [random.gauss(0,0.3)*random.choice([-1,1]) for x in range(len(bottom_100))] #add jitter
x1 += jitter
x2 = np.full_like(top_100, 10)
jitter = [random.gauss(0,0.3)*random.choice([-1,1]) for x in range(len(bottom_100))]
x2 += jitter

# merge the data sets
All_x = np.hstack([x1,x2])
All_data = np.hstack([bottom_100, top_100])

#get mean and SEM
mean_bottom = np.mean(bottom_100)
sem_bottom = np.std(bottom_100)/np.sqrt(len(bottom_100))
mean_top = np.mean(top_100)
sem_top = np.std(top_100)/np.sqrt(len(top_100))

#plot
fig,ax = plt.subplots(1,1, figsize=(8,8))
plt.scatter(All_x, All_data, c='k', alpha=0.5, linewidths=0)
plt.scatter([5,10],[mean_bottom, mean_top], c=['r','b'], s=100)
plt.vlines(5, mean_bottom-sem_bottom, mean_bottom+sem_bottom, color='r')
plt.vlines(10, mean_top-sem_top, mean_top+sem_top, color='b')
ax.set_xticks([5,10])
ax.set_yticks([86,87,88,89,90,91])
ax.set_yticklabels(['60','61','62','63','64','65'])

ax.set_xticklabels(['Δ<<0','Δ>>0'])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_ylabel('Humidity (%)')
plt.xlim(2,13)
plt.show()
 