
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df=pd.DataFrame(ipl_data)
# print(df.sort_values('Points',ascending=False))

#按照年份分组，查看每隔分组信息
grouped=df.groupby('Year')
# print(grouped)
# print(grouped.groups)

#遍历查看每个分组信息
for year,group in grouped:
    # print(year)
    print(group)

#若不希望获取所有分组，如下获取某个分组细节
group=grouped.get_group(2014)
# print(group)

#分组后针对每一组执行整合操作
#(类似数据库中的组函数)
r=grouped['Points'].agg(np.mean)
# print(r,type(r),r.values)                #<class 'pandas.core.series.Series'> 一维数组

#执行多组函数
r1=grouped['Points'].agg([np.mean,np.sum,np.std])
print(r1,type(r1),r1.values)                #<class 'pandas.core.series.Series'> 一维数组



















