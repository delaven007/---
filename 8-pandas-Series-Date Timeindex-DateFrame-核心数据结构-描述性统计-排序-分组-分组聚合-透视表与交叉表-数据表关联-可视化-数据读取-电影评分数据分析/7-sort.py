
import pandas as pd
import numpy as np

# unsorted_df=pd.DataFrame(
#     np.random.randn(10,2),
#     index=[1,4,6,2,3,5,9,8,0,7],
#     columns=['col2','col1']
# 	)
# print(unsorted_df)
#
# #按照行索引标签进行排序
# df=unsorted_df.sort_index(ascending=False)          #ascending升序还是降序，默认升序
# print(df)
#
# #列标签进行排序
# df=unsorted_df.sort_index(axis=1)
# print(df)

#按照某一列进行排序

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

df=pd.DataFrame(d)
print(df)
print('$'*56)
#按照age排序
print(df.sort_values('Age'))


#联合间接排序
print(df.sort_values(['Age','Rating']))


#控制排序顺序
print(df.sort_values(['Age','Rating'],ascending=[True,False]))













