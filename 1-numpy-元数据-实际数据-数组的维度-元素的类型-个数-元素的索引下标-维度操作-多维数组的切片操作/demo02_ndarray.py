"""
demo02_ndarray.py   对象创建
"""
import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a, a.shape)

b = np.arange(1, 10)
print(b)
# 10个0
c = np.zeros(10, dtype='float32')
print(c)
# 3x3个1
d = np.ones((3, 3), dtype='int32')
print(d * 3) 

# 创建一个结构像d的数组，元素都为0
e = np.zeros_like(d)
print(e)

print(np.ones(5) / 5)









