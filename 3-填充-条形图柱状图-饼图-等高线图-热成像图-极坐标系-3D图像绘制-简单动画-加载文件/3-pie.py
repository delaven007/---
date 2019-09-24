"""饼状图"""

import numpy  as np
import matplotlib.pyplot as mp
# mp.figure('pie', facecolor='gray')
#整理数据
#值列表
values=[21,20,27,25,19]
#间距列表
spaces=[0.01,0.01,0.01,0.01,0.01]
#标签列表
labels=['java','js','python','php','C']
#颜色列表
colors=['gold','wheat','red','green','blue']
#创建图形窗口
mp.figure('Pie', facecolor='gray')
#设置标题
mp.title('Pie', fontsize=20)
# 等轴比例
mp.axis('equal')
mp.pie(
    values, 		# 值列表
    spaces, 		# 扇形之间的间距列表
    labels, 		# 标签列表
    colors,
    '%.2f%%',		# 标签所占比例格式
	shadow=True, 	# 是否显示阴影
    # startanle=90  	# 逆时针绘制饼状图时的起始角度
    radius=1		# 半径

)
mp.legend(loc='upper left')
mp.show()



