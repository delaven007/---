"""
demo07_mask.py  掩码
"""
import numpy as np

a = np.arange(1, 100)
# 100以内3的倍数
mask = (a%3 == 0) & (a%7 == 0)
print(a[mask])

# mask 作为下标掩码
b = np.array([90, 80, 60, 30])
mask = np.array([3,2,1,0,1,0,3,2,0,2,0,1])
print(b[mask])

indices = b.argsort()  # 排序后返回有序索引
print(indices)
print(b[indices])



