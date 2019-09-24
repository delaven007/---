
#绘制一条余弦曲线
import numpy as np
import matplotlib.pyplot  as mp

#创建8个数的数组
yarray=np.array([64,89,12,36,49,80,45,34])
#随机抛出8个数
# xarray=np.arange(8)

#画直线工具
mp.plot(yarray)
# mp.show()

# vertical 绘制垂直线
mp.vlines(4, 10, 80)
# horizotal 绘制水平线
mp.hlines(40, 1, 7)
mp.hlines([10,20,30,50],[1,8,4,6],[7,1,5,5])
#显示图表:阻塞函数
mp.show()
















