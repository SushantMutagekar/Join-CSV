import pandas as pd



file1 = pd.read_csv("file1.csv")
file2 = pd.read_csv("file2.csv")

#%%
file1['RTC'] =  pd.to_datetime(file1['RTC'], format='%Y-%m-%d %H:%M:%S')
file2['Time'] =  pd.to_datetime(file2['Time'], format='%d-%b-%y %H:%M:%S:%f')
#%% Reduce precision and make both timestamps in same format

file1['Time'] = file1['RTC'].astype('datetime64[s]')
file2['Time'] = file2['Time'].astype('datetime64[s]')

#%% Sync the times, add offset time to the file2
# let file2 time be ahead by 2minutes 5sec = 125 sec
import datetime
file2['Time'] = file2['Time'] - datetime.timedelta(seconds=125) # seconds =0 if files are already in sync
#%% Left Join both the CSV files to retain all rows of file1 and only the corresponding matcing rows of file2
df_left = pd.merge(file1, file2, on='Time', how='left')
df_left.to_csv("merged_file.csv")