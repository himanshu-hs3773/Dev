from re import T
import pandas as pd
import numpy as np

df1 = pd.read_csv('UK_TopSell.csv')
df1.drop(['Cost', 'In Stock'], axis=1, inplace=True)
df1.sort_values(by=['Item Name'], inplace=True)
# print(df1)

df2 = pd.read_csv('Inventory_0509.csv')
# print(df2)

# res = df1.merge(df2, how='outer', on=['Item Name'])
# res = res.fillna('')

# res['Item Number'] = np.where(res['Item Number_x'] != '', res['Item Number_x'], res['Item Number_y'])
# res = res.drop(['Item Number_x', 'Item Number_y'], axis=1)
# cols = list(res.columns.values)
# res = res[['Item Name',  'Item Number', 'In Stock','Quantity sold', 'Cost',  'Value', 'Price']]


res = pd.merge(df1, df2, on=['Item Name'], how='left')
res.drop(['Unnamed: 1'], axis=1, inplace=True)
# res.set_index('Item Name', inplace=True)
res.to_csv('result2.csv', index=False)
# res = res[['Item Name',  'Item Number', 'Quantity sold', 'Cost',  'Stock', 'Dept']]
print(res)
