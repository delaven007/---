"""矩阵"""

import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
#
# #创建matrix对象
# ary=np.arange(1,10).reshape(3,3)
# print(ary,type(ary))
# ary2=np.matrix(ary,copy=True)
# print(ary2,type(ary2))
#
# ary[0,0]=99
# print(ary2,type(ary2))
#
# #创建matrix对象2
# ary3=np.mat(ary)
# print(ary3)
#
# #创建matrix对象3
# ary4=np.mat('1 2 3; 4 5 6')
# print(ary4,type(ary4))
#
# #矩阵的乘法
# m=np.mat('1 2 6; 3 5 7; 4 8 9')
# print(m**2)
# a=np.array(m)
# # print(a*a)
# # print(a.dot(a))
# # print(a.dot(m))
#
# #逆矩阵
# print(m.I)
# print(m*m.I)
# print(np.linalg.inv(m))
#
# #针对非矩阵
# m=m[:2,:]
# print(m)
# print(m.I)
# print(m*m.I)
# print(np.linalg.inv(m))
#

#解方程
A=np.mat('3 3.2;3.5 3.6')
B=np.mat('118.4;135.2')
x=np.linalg.lstsq(A, B)[0]
print(x)
print(A.I*B)

#矩阵的零次方
print(np.mat('4235 2348;1323 4536')**0)




