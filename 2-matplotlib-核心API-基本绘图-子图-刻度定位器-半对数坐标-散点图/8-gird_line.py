#绘制网格曲线图

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.figure as mg

y=[1,10,100,1000,100,10,1]
mp.figure('Gridline',facecolor='lightgray')

mp.subplot(211)

mp.title('Grid Line',fontsize=16)
#定义刻度定位器
ax=mp.gca()
ma_loc=mp.MultipleLocator(1)
ax.xaxis.set_major_locator(ma_loc)
mi_loc=mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(mi_loc)

ax=mp.gca()
ma_loc=mp.MultipleLocator(250)
ax.yaxis.set_major_locator(ma_loc)
mi_loc=mp.MultipleLocator(50)
ax.yaxis.set_minor_locator(mi_loc)

#绘制刻度网格线
# ax.grid(which='both',axis='both',linewidth=0.75,color='orangered')
ax.grid(which='major',axis='both',linewidth=0.75,color='orangered',alpha=0.8)
ax.grid(which='minor',axis='both',linewidth=0.35,color='coral',alpha=0.8)
mp.plot(y,'o-',color='dodgerblue')


mp.subplot(212)
mp.title('Grid Line',fontsize=16)
#定义刻度定位器
ax=mp.gca()
ma_loc=mp.MultipleLocator(1)
ax.xaxis.set_major_locator(ma_loc)
mi_loc=mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(mi_loc)

ax=mp.gca()
ma_loc=mp.MultipleLocator(250)
ax.yaxis.set_major_locator(ma_loc)
mi_loc=mp.MultipleLocator(50)
ax.yaxis.set_minor_locator(mi_loc)

#绘制刻度网格线
# ax.grid(which='both',axis='both',linewidth=0.75,color='orangered')
ax.grid(which='major',axis='both',linewidth=0.75,color='orangered',alpha=0.8)
ax.grid(which='minor',axis='both',linewidth=0.35,color='coral',alpha=0.8)



mp.semilogy(y,'o-',color='dodgerblue')

mp.show()















