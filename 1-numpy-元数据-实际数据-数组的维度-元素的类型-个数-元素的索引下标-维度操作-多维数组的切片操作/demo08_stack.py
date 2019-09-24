"""
demo08_stack.py  组合与拆分
"""
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

# 水平方向操作
c = np.hstack((a, b))
print(c)
a, b = np.hsplit(c, 2) # 把c沿水平方向拆2份
print(a)
print(b)

# 垂直方向操作
c = np.vstack((a, b))
print(c)
a, b = np.vsplit(c, 2) # 把c沿垂直方向拆2份
print(a)
print(b)

# 深度方向操作
c = np.dstack((a, b))
print(c)
a, b = np.dsplit(c, 2) # 把c沿深度方向拆2份
print(a)
print(b)

# 数组头尾补全
a = np.array([1,2,3,4,5,6])
b = np.array([8,8,8,8])
b = np.pad(b, pad_width=(1,1), mode='constant',
	constant_values=-1)
print(b)

# 一维数组的组合方案:
a = np.arange(10, 20)
b = np.arange(20, 30)
print(a)
print(b)
c = np.row_stack((a, b))
print(c)
d = np.column_stack((a, b))
print(d)



