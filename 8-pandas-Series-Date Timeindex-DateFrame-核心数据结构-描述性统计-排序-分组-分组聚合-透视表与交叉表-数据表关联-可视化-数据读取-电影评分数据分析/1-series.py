import numpy as np
import  pandas as pd

#空series队象
s1=pd.Series()
print(s1)

#通过数组创建Series对象
data=np.array(['zs','ls','ww','zl'])
s2=pd.Series(data)
print(s2)

#修改索引标签
s3=pd.Series(data,index=['s001','s002','s003','s004'])
print(s3)

#从字典创建一个Series
data={'s01':'zs','s02':'ls','s03':'ww'}
s4=pd.Series(data)
print(s4)

#标量创建series
s5=pd.Series(5,index=['a','b','c'])
print(s5)

#从series中读取数据
print('-'*45)
print(s3)
print(s3[0])        #通过下标访问
print(s3[:2])       #通过切片访问
print(s3['s004'])   #通过索引标签

print(s3[['s004','s001']])  #通过索引标签组


#日期
print('-'*45)
data=pd.Series(['2001','2001/1','2001-7-1','2011-1-04 19:59:30','01 Jun 2002'])
s6=pd.to_datetime(data)
print(s6)
delta = s6 - pd.to_datetime('2001-1-1')
print(delta)

#输出日期某些字段的值
print(s6.dt.quarter)
print(delta.dt.days)    #获取偏移天数

# print(s6.dt.year)
# print(s6.dt.month)
# print(s6.dt.day)
# print(s6.dt.hour)
# print(s6.dt.minute)
# print(s6.dt.second)







