"""
demo04_cls.py   复合数据类型
"""
import numpy as np

data = [('zs', [89,96,92], 15), 
		('ls', [81,94,96], 16), 
		('ww', [82,95,97], 17)]

# 指定dtype，告诉ndarray元素类型
ary = np.array(data, dtype='U2,3int32,int32')
print(ary, ary[0][2])

# 第二种设置dtype的方式
ary = np.array(data, dtype=[('name', 'str', 2),
	('scores', 'int32', 3),
	('age', 'int32', 1)])
print(ary, ary[1]['scores'])

# 第三种设置dtype的方式
ary = np.array(data, dtype={
	'names':['name', 'scores', 'age'], 
	'formats':['U2', '3int32', 'int32']})
print(ary, ary[2]['name'])

# 第四种设置dtype的方式
d = np.array(data, dtype={'name': ('U3', 0),
              'scores': ('3int32', 16),
              'age': ('int32', 28)})
print(d[0]['name'], d[0]['scores'], d.itemsize)

# 测试numpy对日期数据的支持
data = ['2011', '2011-01-01', 
		'2012-01-01 08:30:00', '2012-02-01']
data = np.array(data)
print(data, data.dtype)
data = data.astype('M8[D]')
print(data, data.dtype)
print(data[3] - data[2])

