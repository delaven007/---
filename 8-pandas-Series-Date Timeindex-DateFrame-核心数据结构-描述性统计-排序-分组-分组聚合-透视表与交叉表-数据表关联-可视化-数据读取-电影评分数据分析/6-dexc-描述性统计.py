import pandas as pd
import numpy as np

# 创建DF
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack','Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}     #打分
df=pd.DataFrame(d)
print(df.sum())
# print(df.sum(1))            #数字为轴向，按行进行相加
print(df.mean())
# print(df.mean(1))

#输出描述性统计表
print(df.describe())
print('*'*45)
print(df.describe(include=['object']))
print('-'*56)
print(df.describe(include=['number']))











