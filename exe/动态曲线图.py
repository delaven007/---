
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

mp.figure("曲线图",facecolor='lightgray')
mp.xlim(0,10)
mp.ylim(-3,3)
# mp.grid(linestyle='-.',color='gray',alpha=0.5)
pl=mp.plot([],[],color='blue',label='曲线图')[0]
pl.set_data([],[])

x=0
def update(data):
    t,v=data
    x,y=pl.get_data()
    x.append(t)
    y.append(v)
    pl.set_data(x,y)
    # 移动坐标轴
    if (x[-1] > 8):
        mp.xlim(x[-1] - 8, x[-1] + 2)
def y_generator():
    global x
    y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
    yield (x,y)
    x+=0.05
anim=ma.FuncAnimation(mp.gcf(),update,y_generator,interval=50)
mp.tight_layout()
mp.show()




















