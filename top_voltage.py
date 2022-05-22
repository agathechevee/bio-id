import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

''' Find trends in top and bottom 5% recorded Voltage values 
in regards of Independant Variables such as Humidity, 
Temperature and Light '''
#['210721_MFC_recording1.3.csv','220721_MFC_recording_morning.csv','230721_MFC_recording_night.csv']#,
# files = []#'040821_MFC_recorning_night.csv','210721_MFC_recording1.3.csv','220721_MFC_recording_morning.csv','230721_MFC_recording_night.csv']
files = ['060821_night_recording.csv'] #
# files = ['070821_high_humidity.csv']
MFC_extreme = pd.DataFrame()
values_normed = pd.DataFrame() 

def normalize (df):
    scaler= MinMaxScaler()
    norm_array = scaler.fit_transform(df)
    scaled_df = pd.DataFrame(norm_array)
    return scaled_df


def plot_extreme (x, y, extreme):
    n=0
    for columns in x:
        names= ['Humidity','Temp','Light']
        plt.scatter(x=x[columns],y=y["Brick V"], label= names[n])
        n+=1
    plt.legend(loc='best')
    plt.title('%s 15%% current values' %(extreme))
    plt.xlabel('Normalized Independant Variables')
    plt.ylabel('Brick Voltage (V)')
    plt.show()



def top(files,MFC_extreme, values_normed):
    for i in files:   
        print(MFC_extreme)
        df = pd.read_csv(i)
        df = df.rolling(25).mean() 
        df_all = normalize(df).nlargest(18, 0)
        norm_variables = df_all.drop(columns=[0,1,5])
        top20 = df.nlargest(18, 'Brick V')
        top20_V = top20.drop(columns=['Naked T','Humidity','Temp','Light','MFC voltage'])
        MFC_extreme = pd.concat([MFC_extreme,top20_V])
        print(MFC_extreme)
        values_normed = pd.concat([values_normed,norm_variables])
    return values_normed, MFC_extreme

def bottom (files,MFC_extreme, values_normed):
    for i in files:    
        df = pd.read_csv(i)
        df = df.rolling(25).mean() 
        df_all = normalize(df).nsmallest(18, 0)
        norm_variables = df_all.drop(columns=[0,1,5])
        bottom20 = df.nsmallest(18, 'Brick V')
        bottom20_V = bottom20.drop(columns=['Naked T','Humidity','Temp','Light','MFC voltage'])
        MFC_extreme = pd.concat([MFC_extreme,bottom20_V])
        values_normed = pd.concat([values_normed,norm_variables])
    return values_normed, MFC_extreme

def main():
    extreme = 'Top'
    x,y = top(files,MFC_extreme,values_normed)
    print(x,y)
    plot_extreme(x,y,extreme)
    extreme = 'Bottom'
    x,y = bottom(files,MFC_extreme, values_normed)
    plot_extreme(x,y,extreme )
    # print(top(files,MFC_extreme,values_normed))
main()

 
