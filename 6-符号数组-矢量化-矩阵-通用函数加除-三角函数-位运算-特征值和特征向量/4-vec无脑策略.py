"""
4-无脑策略
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

dates,opening_prices,highest_prices,lowest_prices, closeing_prices= np.loadtxt(
    '../data/da_data/aapl.csv',		# 文件路径
    delimiter=',',			# 分隔符
    usecols=(1, 3, 4, 5, 6),			# 读取1、3...两列 （下标从0开始）
    unpack=True,						#是否要拆包True(自动拆)/false(否)
    dtype='M8[D], f8, f8, f8, f8',		# 制定返回每一列数组中元素的类型
    converters={1:dmy2ymd})				#转换器函数字典

# print(dates)
#绘制收盘价的折线图
mp.figure('APPL',facecolor='lightgray')
mp.title('APPL')
mp.xlabel('Date',fontsize=14)
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

#定义买入卖出策略，计算收益率
def profit(opening_price,highest_price,lowest_price,closeing_price):
    buying_price=opening_price * 0.99
    if(highest_price>buying_price>lowest_price):
        return (closeing_price-buying_price)/buying_price
    return np.nan
#计算每天的收益率
profits=np.vectorize(profit)(opening_prices,highest_prices,lowest_prices,closeing_prices)
isnan_mask=np.isnan(profits)
dates,profits=dates[~isnan_mask],profits[~isnan_mask]

# print(np.frompyfunc(foo, 2, 1)(x,y))



#画出线
mp.plot(dates, profits, color='orange',linestyle='-.',label='profits')
#添加图例
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
