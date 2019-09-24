
import pandas as pd

# data=pd.date_range('2019-10-01',periods=7)
# print(data,data.dtype,type(data))
#改变freq，设置频率
data=pd.date_range('2019-10-01',periods=7,freq='M')
print(data,data.dtype,type(data))

#设置生成一组时间:[start,end]
d3=pd.date_range('2002-10-1','2020-9-1',freq='Y')
print(d3)

#生成一组时间，只包含工作日
d4=pd.bdate_range('2019-10-1',periods=7)
print(d4)









