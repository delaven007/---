
"""等高线图"""

import numpy as np
import matplotlib.pyplot as mp

n=1500
#生成网格化坐标矩阵
x,y=np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z=(1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)            #(1+x/2+x**5+y**3)* e**-x**2-y**2

#绘制等高线
mp.figure("Contour", facecolor='wheat')
mp.title('Contour',fontsize=16)
cntr=mp.contour(x,y,z,colors='gold',linewidths=0.5)
#分成8份，不包括（两个）最小的总共8中颜色
mp.contourf(x,y,z,8,cmap='jet')

#为等高线添加标签
mp.clabel(cntr,fmt='%.2f%%',inline_spacing=1,fontsize=10)
mp.show()
















