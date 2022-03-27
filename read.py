import pandas as pd
import numpy as np

### 读取xlsx的文件

p_data = pd.read_excel(r'0322_sue.xlsx',sheet_name='Sheet3')
p_data_mapping = pd.read_excel(r'0322_sue.xlsx',sheet_name='Sheet4')
print(p_data.columns)

### 删除整行为nan
p_data.dropna(axis=0,how='all')
p_data_mapping.dropna(axis=0,how='all')

pd_mapping_result = pd.merge(p_data,p_data_mapping,on = 'Controlling Agent',how="left")
pd_mapping_result['region'].fillna(6.0,inplace=True)
print(pd_mapping_result)

### 分组求和 参考地址： https://www.jb51.net/article/188649.htm







