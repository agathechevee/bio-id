import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sn
from scipy.stats import linregress

df= pd.read_csv('070821_high_humidity2.csv')
x= df['Humidity']
y= df['Brick V'][25:80]
time= list(range (len(y)))
x= sorted([round(random.uniform(52.7, 99), 2) for x in range(70)])
print(linregress(time,y))
fig,ax = plt.subplots(1,1, figsize=(8,6.5))
ax=sn.regplot(x=time,y=y)

plt.scatter(time,y, c='r')
ax.set_xlabel("Time(min)")
ax.set_yticks([0,0.2,0.4,0.6,0.8,1])
ax.spines['left'].set_color('red')
ax.tick_params(axis='y', colors='red')
ax.set_xticklabels(['60','70','80','90','100'])
ax.set_ylabel("Brick voltage (V)")
ax.set_xlim(0,33)
plt.show()