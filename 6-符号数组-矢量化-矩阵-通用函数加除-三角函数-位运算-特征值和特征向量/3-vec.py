"""函数矢量化"""

import numpy as np
import math as m
import matplotlib.pyplot as mp
def foo(x,y):
    return m.sqrt(x**2+y**2)
x,y=4,5
print(foo(x,y))

x=np.array([3,4,5,6])
y=np.array([7,8,9,12])
y=6
# print(foo(x,y))
#foo函数矢量化，返回矢量化函数
foo_vec=np.vectorize(foo)
print(foo_vec(x,y))





