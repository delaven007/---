"""
最值
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

dates,opening_prices,highest_prices,lowest_prices, closeing_prices,volumes= np.loadtxt(
    '../data/da_data/aapl.csv',		# 文件路径
    delimiter=',',			# 分隔符
    usecols=(1, 3, 4, 5, 6,7),			# 读取1、3...两列 （下标从0开始）
    unpack=True,						#是否要拆包True(自动拆)/false(否)
    dtype='M8[D], f8, f8, f8, f8,f8',		# 制定返回每一列数组中元素的类型
    converters={1:dmy2ymd})

#30天的最大震荡幅度
max_prices=np.max(highest_prices)
min_prices=np.min(lowest_prices)
print(min_prices,'~',max_prices)

#哪一天是最高价，哪一天是最低价
max_ind=np.argmax(highest_prices)
min_ind=np.argmin(lowest_prices)
print('min:',dates[min_ind])
print('max:',dates[max_ind])

#
a=np.arange(1,10).reshape(3,3)
b=np.arange(1,10)[::-1].reshape(3,3)
print(np.maximum(a,b))
print(np.minimum(a,b))



# mp.legend()
# mp.gcf().autofmt_xdate()
# mp.show()
