import pandas as pd
import numpy as np

### 读取xlsx的文件
p_data = pd.read_excel(r'0322_sue.xlsx',sheet_name='Sheet2')
print(p_data.columns)

### 删除整行为nan
p_data.dropna(axis=0,how='all')

### 分组求和 参考地址： https://www.jb51.net/article/188649.htm
g_detail = p_data.groupby(by=['Transaction', 'Creditor','Posted','Job']).agg({'Invoiced': sum})
g = p_data.groupby(by=['Transaction', 'Creditor']).agg({'Invoiced': sum})

print(g_detail)
print(g)


##### -----------------






