"""
加   /   乘法  通用函数
"""

import numpy as np
a=np.arange(1,7)
print(a)
print(np.add(a,a))
print(np.add.reduce(a))
print(np.add.accumulate(a))
#整理矩阵（通过列处理数据）
print(np.add.outer([50,60,70],a))       #外和

print(a.prod())
print(a.cumprod())
print(np.outer([40,50,60],a))           #外积


