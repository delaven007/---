"""
wday:   统计周一->周五的收盘价均值
"""

import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    # 把日月年转成周*
    dmy = str(dmy, encoding='utf-8')
    t = dt.datetime.strptime(dmy, '%d-%m-%Y')
    wday = t.date().weekday()
    return wday


wdays, closing_prices = np.loadtxt(
    '../data/da_data/aapl.csv',  # 文件路径
    delimiter=',',
    usecols=(1,6),  # 分隔符
    # usecols=(1, 3, 4, 5, 6, 7),  # 读取1、3...两列 （下标从0开始）
    unpack=True,  # 是否要拆包True(自动拆)/false(否)
    dtype='f8,f8',  # 制定返回每一列数组中元素的类型
    converters={1: dmy2ymd})
ave_prices=np.zeros(5)
# print(ave_prices)
for i in range(ave_prices.size):
        #利用掩码把周一至周五全都遍历出来
    ave_prices[i]=np.mean(closing_prices[wdays==i])
print(ave_prices)

#数组的轴向汇总
prices=closing_prices.reshape(6,5)          #做出一个6行五列的二位数组
print(prices)

def func(ary):
    #数组处理函数         #查看标准差
    return np.mean(ary),np.std(ary)
r=np.apply_along_axis(func,0,prices)
print(' 轴向汇总',np.round(r,2))                    #做四舍五入















