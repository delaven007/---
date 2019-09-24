"""
3-cov-协方差
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
#画出收盘线
mp.plot(dates, bhp_closeing_prices, color='red',alpha=0.8,linestyle='-',label='bhp_closeing_prices')
mp.plot(dates,vale_closeing_prices, color='blue',linestyle='-',alpha=0.8,label='vale_closeing_prices')

#计算两只股票收盘价的平均值
mean_bhp=np.mean(bhp_closeing_prices)
mean_vale=np.mean(vale_closeing_prices)
#计算两只股票收盘价的离差
dev_bhp=bhp_closeing_prices-mean_bhp
dev_vale=vale_closeing_prices-mean_vale
#计算两只股票收盘价的协方差
#样本协方差
# n=bhp_closeing_prices.size
# ycov=(dev_bhp*dev_vale).sum()/(n-1)
# print('cov样本协方差:',ycov)

#总体协方差
zcov=(dev_bhp*dev_vale).mean()
print("cov总体协方差:",zcov)

k=zcov/(zcov/np.std(bhp_closeing_prices)*np.std(vale_closeing_prices))
print('K相关系数:',k)
# 相关矩阵
unp=np.corrcoef(bhp_closeing_prices,vale_closeing_prices)
print("相关矩阵:\n",unp)
# 相关矩阵的分子矩阵
mup=np.cov(bhp_closeing_prices,vale_closeing_prices)
print("相关矩阵的分子矩阵:\n",mup)
#添加图例
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
