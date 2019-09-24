"""开盘价K线"""

import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
import matplotlib.animation as ma

#把日月年转换成年月日
def dmy2ymd(dmy):
    dmy=str(dmy,encoding='utf-8')
    utime=dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    time_=utime.strftime('%Y-%m-%d')
    return time_
#日期/开盘价/最高价/最低价/结束价
dates,opening_prices,highest_prices,lowest_prices,closeing_prices=np.loadtxt(
    './data/da_data/aapl.csv',        #文件路径
    delimiter=',',                     #采用逗号分隔
    usecols=(1,3,4,5,6),               #读取数据列
    unpack=True,                       #拆包
    dtype='M8[D],f8,f8,f8,f8',         #制定返回数据的元素类型
    converters={1:dmy2ymd}             #转换器函数字典
    )
# print(dates)
#绘制收盘价的折线图
mp.figure('APPL',facecolor='lightgray')
mp.title('APPL')
mp.xlabel('Date',fontsize=14)
mp.ylabel('price',fontsize=14)
#网格线
# mp.grid(linestyle='-.')
x,y=0,0
count=2
pl = mp.plot([], [], color='dodgerblue', label='Signal')[0]
pl.set_data([dates[count]],[closeing_prices[count]])
def update(data):
    t, v = data
    global count
    x,y=pl.get_data()
    x.append(t)
    y.append(v)
    count+=1
    pl.set_data(x, y)

def y_generator():
	global x
	global y
	yield (x, y)
	x += 0.05

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
dates=dates.astype(md.datetime.datetime)
#画出开盘价曲线

# mp.plot(dates,opening_prices,color='blue',linestyle='-',alpha=0.6,label='open_prices')



# 绘制五日移动平均线
# 做一个数组
# ma5=np.zeros(closeing_prices.size-4)
# for i in range(ma5.size):
#     #取出平均值
#     ma5[i]=np.mean(closeing_prices[i:i+5])
# mp.plot(dates[4:],ma5,color='yellow',label='MA-5day')

# 卷积10日均线
# kernel=np.ones(10)/10
# ma10=np.convolve(closeing_prices,kernel,'valid')
# mp.plot(dates[9:],ma10,color='purple',label='Ma-10day')
#
# # 卷积20日均线
# kernel=np.ones(20)/20
# ma20=np.convolve(closeing_prices,kernel,'valid')
# mp.plot(dates[19:],ma20,color='cyan',label='Ma-20day')

# 卷积加权30日平均线
# kernel/=kernel.sum()
# #有效卷积
# ma30=np.convolve(closeing_prices,kernel[::-1],'valid')
# mp.plot(dates[29:],ma30,color='purple',label='Ma-30day',linewidth=5)

#整理颜色
# rise=closeing_prices>opening_prices
# #定义颜色#添加图例
# ecolor=np.array( ['red' if x  else 'green' for x in rise ])
# color=np.array(['red' if x  else 'green' for x in rise ])
# # print(ecolor)
# #绘制K线图(柱状图)
# mp.bar(dates,closeing_prices-opening_prices,0.8,opening_prices,edgecolor=ecolor,color=color,zorder=3)
# #绘制影线(|)
# mp.vlines(dates,lowest_prices,highest_prices)
anim = ma.FuncAnimation(mp.gcf(), update,y_generator, interval=10)
mp.tight_layout()
mp.legend()
# mp.gcf().autofmt_xdate()
mp.show()

















