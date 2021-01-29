import pandas as pd

file1 = pd.read_csv("G:\\Python\\Python Basics\\Join-CSV\\file1.csv")
file2 = pd.read_csv("G:\\Python\\Python Basics\\Join-CSV\\file2.csv")

#%% see format in the files and add the format field in below commands
Timeformat_file1 =   '%m/%d/%Y %H:%M:%S'
Timeformat_file2 =  '%d-%b-%y %H:%M:%S:%f'
#file1['new_RTC'] =  pd.to_datetime(file1['RTC'], format='%Y-%m-%d %H:%M:%S')
file1['new_Time'] =  pd.to_datetime(file1['RTC'], format= Timeformat_file1)
file2['new_Time'] =  pd.to_datetime(file2['Time'], format= Timeformat_file2)
#%% Reduce precision and make both timestamps in same format
file1['new_Time'] = file1['new_Time'].apply(lambda t: t.strftime('%d/%m/%Y %H:%M:%S'))
file2['new_Time'] = file2['new_Time'].apply(lambda t: t.strftime('%d/%m/%Y %H:%M:%S'))

#%%
file1['new_Time'] = file1['new_Time'].astype('datetime64[s]')
file2['new_Time'] = file2['new_Time'].astype('datetime64[s]')
#%% Sync the times, add offset time to the file2
# let file2 time be ahead by 2minutes 5sec = 125 sec
import datetime
file2['new_Time'] = file2['new_Time'] - datetime.timedelta(seconds=0) # seconds =0 if files are already in sync

#%% Left Join both the CSV files to retain all rows of file1 and only the corresponding matcing rows of file2
df_left = pd.merge(file1, file2, on='new_Time', how='left')
df_left.to_csv("merged_file.csv")