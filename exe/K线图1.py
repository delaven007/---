
"""开盘价K线"""
import datetime as dt
import matplotlib.dates as md
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma


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


mp.figure("Signal", facecolor='lightgray')
mp.title("Signal", fontsize=14)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle='--', color='lightgray', alpha=0.5)
pl = mp.plot([], [], color='pink', label='Signal')[0]
pl.set_data([],[])
#声明一个变量，用来存储数据
x,y =4, 4

#拿到坐标轴
ax=mp.gca(facecolor='black')
#设置刻度定位器，其中主刻度为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
#设置主刻度标签格式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %y'))
#设置次刻度（一天一次刻度）
ax.xaxis.set_minor_locator(md.DayLocator())
#设置刻度参数（字体大小）
mp.tick_params(labelsize=8,labelcolor='black')

#画出开盘价曲线
mp.plot(x,y,color='blue',linestyle='-',alpha=0.6,label='open_prices')

# 绘制五日移动平均线
# 做一个数组
# ma5=np.zeros(x-4)
# for i in range(ma5.size):
#     #取出平均值
#     ma5[i]=np.mean(x[i:i+5])
# mp.plot(y[4:],ma5,color='yellow',label='MA-5day')




anim = ma.FuncAnimation(mp.gcf(), update,y_generator, interval=3000)
mp.tight_layout()
mp.show()