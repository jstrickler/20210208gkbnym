import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def ceil_time_hour(t):
    return dt.time(max((t.hour + 1),23))

def floor_time_hour(t):
    return dt.time(t.hour)

df = pd.read_csv('timedata.csv')
print(df)
print()
df['timestamp'] = df.apply(lambda x: dt.time(x['hour'], x['minute']), axis=1)
print(df)
print()
df.drop(['hour', 'minute'], axis=1, inplace=True)
print(df)
df.sort_values(by='timestamp', inplace=True)
print(df)
# df.set_index('timestamp', inplace=True)
print(df)
low_time = floor_time_hour(df['timestamp'].min())
high_time = ceil_time_hour(df['timestamp'].max())
df.plot.line('timestamp', 'value')
plt.show()

