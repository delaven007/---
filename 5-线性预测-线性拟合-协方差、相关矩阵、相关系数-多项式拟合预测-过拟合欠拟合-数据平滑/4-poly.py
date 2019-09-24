'''
1. 求出多项式的导函数
2. 求出导函数的根，若导函数的根为实数，则该点则为曲线拐点。
'''
import numpy as np
import matplotlib.pyplot as mp

# x = np.linspace(-20, 20, 1000)
# y = 4*x**3 + 3*x**2  - 1000*x + 1
# Q = np.polyder([4,3,-1000,1])
# xs = np.roots(Q)
# ys =  4*xs**3 + 3*xs**2  - 1000*xs + 1

p=[4,3,-1000,1]
x=np.linspace(-20,20,1000)
#把x带入P,得到函数值y'
y=np.polyval(p,x)

#求导
Q=np.polyder(p)
#求导的根，切线斜率为零时x的值
xs=np.roots(Q)
print(xs)
#根据拟合系数与自变量求出拟合值, 由此可得拟合曲线坐标样本数据
ys=np.polyval(p,xs)
print(ys)
mp.plot(x, y)
mp.scatter(xs, ys, s=80, c='orangered')
mp.show()