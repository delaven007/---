"""
std:标准差
"""

import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    # 把日月年转成年月日
    dmy = str(dmy, encoding='utf-8')
    t = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    s = t.strftime('%Y-%m-%d')
    return s


dates, opening_prices, highest_prices, lowest_prices, closeing_prices, volumes = np.loadtxt(
    '../data/da_data/aapl.csv',  # 文件路径
    delimiter=',',  # 分隔符
    usecols=(1, 3, 4, 5, 6, 7),  # 读取1、3...两列 （下标从0开始）
    unpack=True,  # 是否要拆包True(自动拆)/false(否)
    dtype='M8[D], f8, f8, f8, f8,f8',  # 制定返回每一列数组中元素的类型
    converters={1: dmy2ymd})

std_c=np.std(closeing_prices)
print(std_c)
std_o=np.std(opening_prices)
print(std_o)
std_c2=np.std(closeing_prices,ddof=1)
print(std_c2)

#手动实现
m=np.mean(closeing_prices)
d=closeing_prices - m
v=np.mean(d**2)
s=np.sqrt(v)
print(s)        #总体标准差

v2=(d**2).sum()/(d.size-1)
s2=np.sqrt(v2)
print(s2)       #样本标准差



# mp.legend()
# mp.gcf().autofmt_xdate()
# mp.show()
