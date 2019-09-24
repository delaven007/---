#填充：绘制两条曲线

import numpy as np
import matplotlib.pyplot as mp

x=np.linspace(0,8*np.pi,1000)
sinx=np.sin(x)
cosx=np.cos(x/2)/2

mp.figure('Fill',facecolor='lightgray')
mp.title('Fill',fontsize=16)
mp.grid(linestyle=':')
mp.plot(x,sinx,color='dodgerblue',label='sinx')
mp.plot(x,cosx,color='orangered',label='cosx')

#填充
mp.fill_between(x,sinx,cosx,sinx<cosx,color='dodgerblue',alpha=0.2)


mp.legend()
mp.show()



