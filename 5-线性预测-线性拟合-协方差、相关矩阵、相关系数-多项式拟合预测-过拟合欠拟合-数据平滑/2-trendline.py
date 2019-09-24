"""
2-trendline:趋势线
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
#画出线
mp.plot(dates, opening_prices, color='dodgerblue',linestyle='-.',label='open-price')

#整理每天的趋势价格绘制趋势线,拟合得到的趋势线
trend_points=(highest_prices+lowest_prices+closeing_prices)/3
mp.scatter(dates,trend_points,s=70,color='orangered',label='trend points')
#整理A和B
days=dates.astype('M8[D]').astype('i4')
#让x与一组1进行列合并
A=np.column_stack((days,np.ones(days.size)))
B=trend_points
x=np.linalg.lstsq(A,B)[0]
#将日期带入线性模型方程，得到每天趋势价格
trend_points=x[0]*days +x[1]
mp.plot(dates,trend_points,color='red',label='Trend Line')
#绘制底部支撑线
# trend_points = (highest_prices + lowest_prices + closeing_prices) / 3
# spreads = highest_prices - lowest_prices
# support_points = trend_points - spreads
# days = dates.astype(int)
# x = np.linalg.lstsq(a, support_points)[0]
# support_line = days * x[0] + x[1]
# mp.scatter(dates, support_points, c='limegreen', alpha=0.5, s=60, zorder=2)
# mp.plot(dates, support_line, c='limegreen', linewidth=3, label='Support')


#添加图例
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
