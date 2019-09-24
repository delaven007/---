"""
加载文件
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

# 整理五元一次方程组    最终获取一组股票走势预测值
N = 1
pred_prices = np.zeros(closeing_prices.size - 2 * N + 1)
for i in range(pred_prices.size):
    A = np.zeros((N, N))
    for j in range(N):
        A[j,] = closeing_prices[i + j:i + j + N]                        #1 2 3
    B = closeing_prices[i + N:i + N * 2]                                #6 7 8
    x = np.linalg.lstsq(A, B)[0]
    pred_prices[i] = x.dot(B)  # 点积： x[0]*d+x[1]*e+x[2]*f

# 由于预测的是下一天的收盘价，所以想日期数组中追加一个元素，为下一个工作日的日期
# dates = dates.astype(md.datetime.datetime)
# mp.plot(dates, closeing_prices, 'o-', c='lightgray', label='Closing Price')
# dates = np.append(dates, dates[-1] + pd.tseries.offsets.BDay())
mp.plot(dates[2 * N:], pred_prices[:-1], 'o-', c='orangered',
        linewidth=3, label='Predicted Price')
print(pred_prices[:-1])


#添加图例
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
