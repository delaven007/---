
"""
简单动画：心电图
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma


mp.figure("Signal", facecolor='lightgray')
# mp.title("Signal", fontsize=14)
#设定初始x坐标轴的范围
mp.xlim(5, 10)
#设定初始y坐标轴的范围
mp.ylim(-3, 3)
mp.grid(linestyle='--', color='lightgray', alpha=0.5)
pl = mp.plot([], [], color='dodgerblue', label='Signal')[0]
pl.set_data([],[])
#
x = 0

def update(data):
	t, v = data
	x, y = pl.get_data()
	x.append(t)
	y.append(v)
	#重新设置数据源
	pl.set_data(x, y)
	#移动坐标轴
	if(x[-1]>8):
		mp.xlim(x[-1]-8, x[-1]+2)


def y_generator():
	global x
	y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
	yield (x, y)
	x += 0.05

ma5=np.zeros(y-4)
for i in range(ma5.size):
    #取出平均值
    ma5[i]=np.mean(y[i:i+5])
mp.plot(x[4:],ma5,color='yellow',label='MA-5day')



anim = ma.FuncAnimation(mp.gcf(), update,y_generator, interval=30)
mp.tight_layout()
mp.show()