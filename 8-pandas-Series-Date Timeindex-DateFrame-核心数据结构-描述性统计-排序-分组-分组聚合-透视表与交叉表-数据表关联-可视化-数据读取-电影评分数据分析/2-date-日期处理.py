
import pandas as pd

# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01',
                   '2011/05/01 01:01:01', '01 Jun 2011'])
# to_datetime() 转换日期数据类型
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
# datetime类型数据支持日期运算
delta = dates - pd.to_datetime('1970-01-01')
# 获取天数数值
print(delta.dt.days)