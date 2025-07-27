import pandas as pd

df1 = pd.read_csv('datasets/order_kpi_feed.csv')
df2 = pd.read_csv('datasets/orders_raw.csv')

newdf = pd.merge(df1, df2, how="outer", indicator=True)
discrepancy = newdf.loc[newdf['_merge'] == 'right_only']

print(discrepancy)