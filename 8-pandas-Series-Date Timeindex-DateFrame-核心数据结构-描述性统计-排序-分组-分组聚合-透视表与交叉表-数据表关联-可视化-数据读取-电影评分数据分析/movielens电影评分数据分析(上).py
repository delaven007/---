import numpy as np
import pandas as pd

users = pd.read_table('users.dat', header=None, names=['UserID','Gender','Age','Occupation','Zip-code'], sep='::',engine='python')

# 打印列表长度，共有6040条记录
# print(len(users))
# 查看前五条记录
# print(users.head(5))

# 同样方法，导入电影评分表
ratings = pd.read_table('ratings.dat', header=None, names=['UserID', 'MovieID', 'Rating', 'Timestamp'], sep='::',engine='python')
# 打印列表长度
# print(len(ratings))
# print(ratings.head(5))
# 同样方法，导入电影数据表
movies = pd.read_table('movies.dat', header=None, names=['MovieID', 'Title', 'Genres'], sep='::',engine='python')
# print(len(movies))
# print(movies.head(5))

# 导入完成之后，我们可以发现这三张表类似于数据库中的表
# 要进行数据分析，我们就要将多张表进行合并才有助于分析 先将users与ratings两张表合并再跟movied合并
data = pd.merge(pd.merge(users, ratings), movies)
# print(data.head(10))

#描述分析
# data.describe()

# data.info()

# 合并后的每一条记录反映了每个人的年龄，职业，性别，邮编，电影ID，评分，时间戳，电影信息，电影分类等一系列信息
# 比如我们查看用户id为12的所有信息
print([data.UserID==12])






