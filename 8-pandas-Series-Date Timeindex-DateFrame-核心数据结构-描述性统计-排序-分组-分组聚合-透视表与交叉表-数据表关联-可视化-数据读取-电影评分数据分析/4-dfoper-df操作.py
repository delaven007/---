
import pandas as pd
import numpy as np

data={'Name':['Tom','jerry','dabai'],'age':[15,20,11]}
df=pd.DataFrame(data,index=['01','02','03'])
# print(df)

#访问Name列
# print(df['Name'])
# print(df['age'])


#列添加score列
df['score']=pd.Series([90,56,91],index=['01','03','02'])
print(df)

#删除列
# del(df['score'])
# df.pop('age')
# print(df)

# print('-'*45)
#
# #行访问
# print(df[:2])       #前两行
# print(df.loc['01'])         #通过索引标签名
# print(df.loc[['01','02']])         #通过索引标签组
# print(df.iloc[0])
# print(df.iloc[[0,2]])

#行添加
# print('*'*45)
# print(df)
# df=df.append(df)
# print(df)
# print(df.loc['01'])

#行删除
print('^'*56)
print(df)
df=df.drop('02')
print(df)

#修改元素
df['Name'][0]='lucy'
print(df)












