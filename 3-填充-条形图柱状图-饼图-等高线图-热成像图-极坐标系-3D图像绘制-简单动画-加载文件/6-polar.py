"""极坐标系"""

import numpy as np
import matplotlib.pyplot as mp


t=np.linspace(0,4*np.pi,1000)
r=0.8*t
mp.figure('Polar',facecolor='lightgray')
#写入极坐标系
mp.gca(projection='polar')
mp.title('Polar',fontsize=16)
mp.xlabel(r'$theta$')
mp.ylabel(r'$\rho$')
mp.grid(linestyle=':')
mp.plot(t,r)
#在极坐标系中绘制正弦函数
x = np.linspace(0, 6*np.pi, 1000)
y = 3*np.sin(6*x)
mp.plot(x, y)
mp.show()










