"""
绘制K线图
"""

import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

def dmy2ymd(dmy):
    #把日月年转成年月日
    dmy=str(dmy,encoding='utf-8')
    t=dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    s=t.strftime('%Y-%m-%d')
    return s
                                                                #从文本中取出各个数据
dates,opening_prices,highest_prices,lowest_prices, closeing_prices= np.loadtxt(
    '../data/da_data/aapl.csv',		# 文件路径
    delimiter=',',			# 分隔符
    usecols=(1, 3, 4, 5, 6),			# 读取1、3...两列 （下标从0开始）
    unpack=True,						#是否要拆包True(自动拆)/false(否)
    dtype='M8[D], f8, f8, f8, f8',		# 制定返回每一列数组中元素的类型
    converters={1:dmy2ymd})				#转换器函数字典(对读取的数据进行预处理)
# print(dates,opening_prices,highest_prices,lowest_prices, closeing_prices)
# print(dates)
#绘制收盘价的折线图
mp.figure('APPL',facecolor='lightgray')
mp.title('APPL')
#x轴标题
mp.xlabel('Date',fontsize=14)
#y轴标题
mp.ylabel('price',fontsize=14)
mp.grid(linestyle=':')

#拿到坐标轴
ax=mp.gca()
#设置主刻度定位器为周定位器（每周一显示主刻度文本）
#设置刻度定位器
#每周一个主刻度，一天一个次刻度
ax.xaxis.set_major_locator( md.WeekdayLocator(byweekday=md.MO) )
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))

#设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())
mp.tick_params(labelsize=8)
dates = dates.astype(md.datetime.datetime)
#画出线
mp.plot(dates, opening_prices, color='dodgerblue',linestyle='-',label='peru')
#添加图例

#整理颜色
rise=closeing_prices>opening_prices
#定义颜色
ecolor=np.array( ['red' if x  else 'green' for x in rise ])
color=np.array(['white' if x  else 'white' for x in rise ])
print(ecolor)
#绘制K线图(柱状图)
mp.bar(dates,closeing_prices-opening_prices,0.8,opening_prices,edgecolor=ecolor,color=color,zorder=3)
#绘制影线(|)
mp.vlines(dates,lowest_prices,highest_prices)


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
