
#散点图
import numpy as np
import matplotlib.pyplot as mp
#生成一组符合正态分布的随机数
n=500
x=np.random.normal(173,4.5,n)       #身高
y=np.random.normal(60,10,n)         #体重

mp.figure("Scatter" ,facecolor='lightgray')
mp.title('Persons',fontsize=16)
mp.xlabel("Height",fontsize=14)
mp.ylabel("Weight",fontsize=14)
d=(x-173)+(y-60)
mp.scatter(x,y,c=d,cmap='jet_r',label='Persons',s=20)         #此处不能放c开头的属性参数
mp.legend()
mp.show()












