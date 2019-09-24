"""热成像图"""
import numpy as np
import matplotlib.pyplot as mp

n=500
#生成网格化坐标矩阵
x,y=np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z=(1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)            #(1+x/2+x**5+y**3)* e**-x**2-y**2
#绘制热成像
mp.figure("Imshow", facecolor='wheat')
mp.title('Imshow',fontsize=16)
# 把矩阵z图形化，使用cmap表示矩阵中每个元素值的大小
# origin: 坐标轴方向
#    upper: 缺省值，原点在左上角
#    lower: 原点在左下角
cntr=mp.imshow(z,cmap='jet',origin='lower')
#添加颜色条
mp.colorbar()
mp.show()
















