
#九框分隔
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Subplot',facecolor='lightgray')
for i in range(9):
    mp.subplot(3,3,i+1)
    mp.text(0.5,0.5,i+1,ha='center',va='center',size='36',alpha=0.8)
    mp.tight_layout()
    #设置刻度为空
    mp.xticks([])
    #隐藏刻度
    mp.yticks([])
mp.show()
















