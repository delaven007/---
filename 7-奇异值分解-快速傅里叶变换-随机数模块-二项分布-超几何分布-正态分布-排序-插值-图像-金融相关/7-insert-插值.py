"""7-insert-插值"""

# scipy.interpolate
import scipy.interpolate as si
import numpy as np
import matplotlib.pyplot as mp

# 原始数据 11组数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 11)
dis_y = np.sinc(dis_x)

# 通过一系列的散点设计出符合一定规律插值器函数，使用线性插值（kind缺省值）
linear = si.interp1d(dis_x, dis_y)
lin_x = np.linspace(min_x, max_x, 1000)
lin_y = linear(lin_x)
mp.plot(lin_x,lin_y)
# 三次样条插值 （CUbic Spline Interpolation） 获得一条光滑曲线
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
cub_x = np.linspace(min_x, max_x, 1000)
cub_y = cubic(cub_x)
mp.plot(cub_x,cub_y)
#绘制线性插值函数
# linear=si.interp1d(dis_x,dis_y)
# x=linear(np.linspace(min_x,max_x,1000))
# y = linear(x)

mp.scatter(dis_x,dis_y,color='blue')
mp.show()






