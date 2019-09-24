"""
demo05_shape.py 维度操作
"""
import numpy as np
# 视图变维
a = np.arange(1, 10)
print(a, a.shape)
a = a.reshape(3, 3)
print(a, a.shape)
b = a.ravel()
print(b, b.shape)
b[0] = 999
print(a, a.shape)  # 视图变维，数据共享

# 复制变维
c = a.flatten()   # c[999, 2, 3, 4...]
print(c)
a[0][0] = 1
print(c)

#就地变维
a.shape = (-1, 9)
print(a, a.shape)
a.resize(3, 3)
print(a, a.shape)




