from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from random import seed
import random
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm
import seaborn as sn
 
df= pd.read_csv('070821_high_humidity.csv')
# df = pd.read_csv('210721_MFC_recording1.3.csv')
time= range (120)

y= sorted([round(random.uniform(50, 99), 2) for x in range(120)])
model = LinearRegression().fit(y,df['Brick V'])
plt.scatter(time, df['Brick V'], c='k', alpha=0.5, linewidths=0.1)

plt.scatter(time,df['Humidity'], c='r')
sn.set(color_codes=True)
ax=sn.regplot(x=x,y=y,x_bins=5)
plt.show()

# The coefficients
print('Coefficients: \n', model.coef_)
The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(diabetes_y_test, diabetes_y_pred))
df=pd.DataFrame({'X': range(1,940), 'Y': np.random.randn(100)*15+range(1,101), 'Z': (np.random.randn(100)*15+range(1,101))*2 })
print(sorted(y))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, df['Brick V'], c='blue')
ax.plot_surface(x, y, df['Brick V'], cmap=cm.coolwarm,
                      ax.scatter(x, y, df['Brick V'], c='blue', s=60)

ax.view_init(30, 285)
ax.set_title("Voltage variation over increasing humidity")
ax.set_xticks([0,200,400,600,800])
ax.set_xticklabels(['0.5h', '1h', '1.5h', '2h','2.5h'])

ax.set_xlabel("Time")
ax.set_ylabel("Humidity (%)")
ax.set_zlabel("Brick 50/50 current (V)")
plt.show()

