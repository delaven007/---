
import pandas as pd

data={'Name':['Tom','jerry','dabai'],'age':[15,20,11],'score':[80,95,96]}
df=pd.DataFrame(data,index=['01','02','03'])
print(df)
print(df.axes)      #行列的索引标签
print(df['age'].dtype)
print(df.empty)
print(df.ndim)                  #底层数据的维数
print(df.size)
print(df.values,type(df.values))
print(df.head(2))
print(df.tail(3))

















