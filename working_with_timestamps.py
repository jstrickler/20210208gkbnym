import pandas as pd
import datetime
import matplotlib.pyplot as plt

def ceil_time(t, delta):
    return t + (t.min - t) % delta


df = pd.read_csv('timedata.csv')
print(df)
print()
df['timestamp'] = df.apply(lambda x: datetime.time(x['hour'], x['minute']), axis=1)
print(df)
print()
df.drop(['hour', 'minute'], axis=1, inplace=True)
print(df)
df.sort_values(by='timestamp', inplace=True)
print(df)
# df.set_index('timestamp', inplace=True)
print(df)
high_time = ceil_time(df['timestamp'].max(), 3600)
print(high_time)
df.plot('timestamp', 'value')
plt.show()

