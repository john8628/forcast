import pandas as pd
import numpy as np


#### 第一部分
### 读取xlsx的文件
p_data = pd.read_excel(r'0322_sue.xlsx',sheet_name='Sheet2')
#print(p_data.columns)

### 删除整行为nan
p_data.dropna(axis=0,how='all')

p_data = p_data.loc[(p_data['Posted'] >= pd.to_datetime("2022-03-21 00:00:00")) & (p_data['Posted'] <= pd.to_datetime("2022-03-27 23:59:59"))]


### 分组求和 参考地址： https://www.jb51.net/article/188649.htm
g_detail = p_data.groupby(by=[ 'Creditor','Posted','Job']).agg({'Invoiced': sum})
g_detail_1 = p_data.groupby(by=[ 'Creditor']).agg({'Invoiced': sum})

print(g_detail.columns.tolist())
g_detail.to_csv('result.csv')
g_detail_1.to_csv('result1.csv')
## g = p_data.groupby(by=['Transaction', 'Creditor']).agg({'Invoiced': sum})
#resDF = g_detail.loc[(g_detail['Posted'] >= "2022-03-21") & (g_detail['Posted'] <= "2022-03-27")]

##g_detail[pd.date_range('2022-03-21','2022-03-27')]










#### 第二部分

### 读取xlsx的文件
p_data_2 = pd.read_excel(r'0322_sue.xlsx',sheet_name='Sheet1')
print(p_data_2.columns)


### 删除整行为nan
p_data_2.dropna(axis=0,how='all')
print(p_data_2)

for index,row in p_data_2.iterrows():
    x = row['cash_3_21_3_27']
    if x == np.NaN:
        continue
    print(x)
    ##g_detail.fillna()
    #pd_all = g_detail[(g_detail['Creditor'] == x)]
    pd_all = g_detail.query('Creditor==' + str(x))
    print(pd_all)



##### -----------------







