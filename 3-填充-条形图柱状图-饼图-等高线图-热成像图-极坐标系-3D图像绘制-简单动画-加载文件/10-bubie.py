"""
简单动画：冒泡
"""

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

#随机生成100个泡泡，并且初始化所有属性
n=100
balls=np.zeros(100,dtype=[
    ('position','f8',2),
    ('size','f8',1),
    ('growth','f8',1),
    ('color','f8',4)
])
balls['position']=np.random.uniform(0,1,(n,2))
balls['size']=np.random.uniform(n,n,n)
balls['growth']=np.random.uniform(n,n-n,n)
balls['color']=np.random.uniform(0,1,(n,4))
# for ball in balls:
#     print(ball)

#绘制图像
mp.figure('Animation',facecolor='lightgray')
mp.title('Animation',fontsize=16)
mp.xticks([])
mp.yticks([])               #所有行的第一列
sc=mp.scatter(balls['position'][:,0],
                            #所有行的第二列
           balls['position'][:,1],
           s=balls['size'],
           color=balls['color'],alpha=0.5)
#定义并执行动画
def update(number):
    #更新每个泡泡size
    balls['size'] +=balls['growth']
    sc.set_sizes(balls['size'])
    #选择一个点，重新初始化属性
    index=number%100
    #大小
    balls[index]['size']= np.random.uniform(40,100,1)
    #位置
    balls[index]['position']=np.random.uniform(0,1,(1,2))
    #重新设置大小和位置
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])
anim=ma.FuncAnimation(mp.gcf(),update,interval=10)


ma.FuncAnimation(mp.gcf(),update,interval=10)
mp.show()