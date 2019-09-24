"""
基本绘图
"""
import numpy as np
import matplotlib.pyplot as mp

#绘制正弦曲线
#从负π到π拆1000个点
x=np.linspace(-np.pi,np.pi,1000)
#正弦曲线
sinx=np.sin(x)
#余弦曲线
cosx=np.cos(x)
mp.vlines(0,-1,1)
mp.hlines(0,-np.pi,np.pi)
#绘制两条数轴线                                                          #定义标签
mp.plot(x,sinx,linestyle='--',linewidth=3,color='wheat',alpha=0.8,label=r'$y=sin(x)$')
mp.plot(x,cosx,linestyle='-.',linewidth=3,color='sienna',alpha=0.8,label=r'$y=\{1}{2}cos(x)$')
#绘制特殊点
xs=[np.pi/2,np.pi/2]
ys=[1,0]
mp.scatter(xs,ys,marker='o',edgecolor='blue',facecolor='green',s=80,label='star',zorder=4)

#添加备注
mp.annotate(
    r'$[\frac{\pi}{2}]$',			#备注中显示的文本内容
    xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(np.pi/2,1),	 				#备注目标点的坐标
    textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(20,15),				#备注文本的坐标
    fontsize=14,				#备注文本的字体大小
    arrowprops=dict(arrowstyle='->',connectionstyle='arc')			#使用字典定义文本指向目标点的箭头样式
)





#显示图例+设置图例的位置
mp.legend(loc='best')
# mp.show()

#设置可视区间
mp.xlim(0,np.pi+0.1)
mp.ylim(0,1+0.1)
# mp.show()

#把横坐标的刻度显示为：0, π/2, π, 3π/2, 2π
x_val_list=[-np.pi,-np.pi/2,0, np.pi/2, np.pi, np.pi/2, np.pi]
x_text_list=[r'$-\pi$',r'$-\frac{\pi}{2}$','0','π/2',r'$\pi$']
#修改x轴y轴刻度
mp.xticks(x_val_list,x_text_list)
mp.yticks([-1.0,-0.5,0,0.5,1.0])
# mp.show()

#移动坐标轴
axis=mp.gca()
axis.spines['top'].set_color('none')
axis.spines['right'].set_color('none')
axis.spines['left'].set_position(('data',0))
axis.spines['bottom'].set_position(('data',0))

mp.show()



