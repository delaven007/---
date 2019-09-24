
import pandas as pd

#以字典的方式构建df
data={'name':['Tom','Jack','Steve'],'Age':[ 15,   16,   19]}
df=pd.DataFrame(data,index=['s01','s02','s03'])
print(df)


data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)












