"""
6-ph-数据平滑
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

dates, bhp_closeing_prices= np.loadtxt(
    '../data/da_data/bhp.csv',		# 文件路径
    delimiter=',',			        # 分隔符
    usecols=(1, 6),			        # 读取1、3...两列 （下标从0开始）
    unpack=True,					#是否要拆包True(自动拆)/false(否)
    dtype='M8[D], f8',		        # 制定返回每一列数组中元素的类型
    converters={1:dmy2ymd})			#转换器函数字典

vale_closeing_prices= np.loadtxt(
    '../data/da_data/vale.csv',		# 文件路径
    delimiter=',',			        # 分隔符
    usecols=(6),			        # 读取1、3...两列 （下标从0开始）
    unpack=True,					#是否要拆包True(自动拆)/false(否)
    dtype='f8'		        # 制定返回每一列数组中元素的类型
)

#绘制收盘价的折线图
mp.figure('COV',facecolor='lightgray')
mp.title('COV')
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

#计算收益，绘制曲线
bhp_returns=np.diff(bhp_closeing_prices)/bhp_closeing_prices[:-1]
vale_returns=np.diff(vale_closeing_prices)/vale_closeing_prices[:-1]

mp.plot(dates[1:],bhp_returns,color='blue',label='bhp returns',alpha=0.2)
mp.plot(dates[1:],vale_returns,color='red',label='vale returns',alpha=0.2)

#卷积降噪
kernel=np.hanning(8)
kernel/=kernel.sum()
bhp_convoloed=np.convolve(bhp_returns,kernel,'valid')
vale_convoloed=np.convolve(vale_returns,kernel,'valid')

mp.plot(dates[8:],bhp_convoloed,color='orange',label='bhp_convoloed',alpha=0.1)
mp.plot(dates[8:],vale_convoloed,color='m',label='vale_convoloed',alpha=0.1)

#多项式拟合，获取两项多项式系数
days=dates[8:].astype('M8[D]').astype('i4')
bhp_P=np.polyfit(days,bhp_convoloed,3)
bhp_val=np.polyval(bhp_P,days)                              #把days带入polyval
vale_P=np.polyfit(days,vale_convoloed,3)
vale_val=np.polyval(vale_P,days)
mp.plot(dates[8:],bhp_convoloed,color='gold',label='bhp_convoloed')
mp.plot(dates[8:],vale_convoloed,color='green',label='vale_convoloed')

#求两个多项式的焦点
diff_P=np.polysub(bhp_P,vale_P)
#求根
xs=np.roots(diff_P)
print(xs.astype('M8[D]'))

#添加图例
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
