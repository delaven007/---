"""
窗口
"""
import numpy as np
import matplotlib.pyplot as mp

#新建一个窗体1
mp.figure('Figure1',facecolor='gray')
#为Figure1添加标题
mp.title('Figure 1')
#新建窗口2
mp.figure('Figure2',facecolor='lightgray')
#为Figure2添加标题
mp.title('Figure 2')

#把Figure1置位当前窗口
mp.figure('Figure1')
mp.title('Figure 1',fontsize=20)
#刻度参数       刻度标签文本大小
mp.tick_params(labelsize=10)
#设置x轴文本
mp.xlabel('X',fontsize=16)
#设置y轴文本
mp.ylabel('Y',fontsize=16)
#设置图标网格线
mp.grid(linestyle=':')
#调用Figure2
mp.figure('Figure2')
mp.title('Figure 2',fontsize=20)
#设置x轴文本
mp.xlabel('X',fontsize=16)
#设置y轴文本
mp.ylabel('Y',fontsize=16)
#设置图标网格线
mp.grid(linestyle=':')

#图标或者字体太小或者字体重合用紧凑
mp.tight_layout()       #紧凑布局
mp.show()




