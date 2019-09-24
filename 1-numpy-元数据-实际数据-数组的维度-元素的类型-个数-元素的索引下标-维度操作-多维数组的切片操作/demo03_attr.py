"""
demo03_attr.py   ndarray的属性
"""
import numpy as np

# 维度
ary = np.arange(1, 7)
print(ary, ary.shape)
ary.shape = (2, 3)
print(ary, ary.shape)

# 元素的数据类型   
# 0000 0000 0000 0000 0000 0000 0000 0001
print(ary, ary.dtype)
# ary.dtype = 'int64'
# print(ary, ary.dtype)
ary = ary.astype('float64')
print(ary, ary.dtype)

# 数组长度
print(ary)
print('size:', ary.size, ' len:', len(ary))

# 数组的索引
a = np.arange(1, 19)
a.shape = (3, 2, 3)    #页、行、列
print(a)
print(a[1][0][1], a[1, 0, 1])

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i, j, k])
